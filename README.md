# OctoPrint_CLI-StatMonitor

## Overview

This Python script fetches information about the current print job from the OctoPrint API and displays progress, time remaining, time elapsed, and other details using the "toilet" command to format it neatly.

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- "toilet" command (install it using your package manager, e.g., `apt install toilet`)

## Configuration

1. Replace the placeholder API key with your OctoPrint API key:

    ```python
    API_KEY = "YOUR_OCTOPRINT_API_KEY"
    ```

2. Replace the placeholder OctoPrint server IP with your server's IP:

    ```python
    OCTOPRINT_IP = "YOUR_OCTOPRINT_SERVER_IP"
    ```

## Usage

1. Make sure you have Python 3 installed.

2. Install the required `requests` library:

    ```bash
    pip install requests
    ```

3. Install the "toilet" command using your system's package manager:

    ```bash
    # For example, on Debian-based systems
    sudo apt install toilet
    ```

4. Run the script:

    ```bash
    python progress-indicator.py
    ```

   The script will continuously fetch and display information about the print job every 10 seconds.

## Customization

- **Font:** You can customize the font used by the "toilet" command. Change the `-f` flag in the `command` variable:

    ```python
    command = f"toilet -t -f term -F border -- '{info_str}'"
    ```

   Replace `"term"` with the font of your choice. You can explore available fonts using:

    ```bash
    toilet -F list
    ```

- **Interval:** Adjust the sleep interval in the script to update the information more or less frequently:

    ```python
    time.sleep(10)  # Adjust the interval as needed
    ```

## To-do

Add the ability to output the most recent chat from a Twitch stream.
