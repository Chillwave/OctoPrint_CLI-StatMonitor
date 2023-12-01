# OctoPrint_CLI-StatMonitor

import requests
import subprocess
import time

API_KEY = "addYourKey"  # Replace with your OctoPrint API key
OCTOPRINT_IP = "127.0.0.1"  # Replace with your OctoPrint server IP

def get_print_info():
    url = f"http://{OCTOPRINT_IP}/api/job"
    headers = {"Content-Type": "application/json", "X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        filename = data["job"]["file"]["name"]
        progress = round(data["progress"]["completion"], 2)
        
        # Check if time_remaining_seconds is available
        if "printTimeLeft" in data["progress"]:
            time_remaining_seconds = data["progress"]["printTimeLeft"]
            time_remaining_minutes = round(time_remaining_seconds / 60, 2)
        else:
            time_remaining_minutes = None
        
        time_elapsed_seconds = data["progress"]["printTime"]
        time_elapsed_minutes = round(time_elapsed_seconds / 60, 2)
        return filename, progress, time_remaining_minutes, time_elapsed_minutes
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to OctoPrint API: {e}")
        return None, None, None, None

def display_info(filename, progress, time_remaining, time_elapsed):
    if filename is not None and progress is not None:
        info_str = f"File: {filename}\nProgress: {progress}%"
        
        # Check if time_remaining and time_elapsed are available
        if time_remaining is not None:
            info_str += f"\nTime Remaining: {time_remaining} minutes"
        if time_elapsed is not None:
            info_str += f"\nTime Elapsed: {time_elapsed} minutes"

        command = f"toilet -t -f term -F border -- '{info_str}'"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    while True:
        filename, progress, time_remaining, time_elapsed = get_print_info()
        display_info(filename, progress, time_remaining, time_elapsed)
        time.sleep(10)  # Adjust the interval as needed
