import subprocess
import re


import platform

def get_windows_wifi_passwords():
    try:
        # Run the command to get saved WiFi profiles
        result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True, check=True)

        # Extract profile names
        profile_names = re.findall(r"\s+:\s(.*)", result.stdout)

        # If no profiles found, print a message
        if not profile_names:
            print("No WiFi profiles found.")
            return

        # Iterate through profiles and retrieve passwords
        for name in profile_names:
            # Run the command to get details of each profile
            profile_result = subprocess.run(["netsh", "wlan", "show", "profile", name.strip(), "key=clear"],
                                            capture_output=True, text=True, check=True)

            # Extract password using regular expression
            password_match = re.search(r"Key Content\s+:\s(.*)", profile_result.stdout)
            password = password_match.group(1) if password_match else "Password not found"

            print(f"WiFi Name: {name.strip()}, Password: {password}")

    except subprocess.CalledProcessError as e:
        print("Error:", e)

import os

def get_macos_wifi_passwords():
    if os.geteuid() != 0:
        print("Tip: Run with 'sudo python3 get_wifi.py' to potentially avoid Keychain prompts.\n")

    try:
        # Get all saved Wi-Fi networks
        # Note: This assumes the Wi-Fi interface is en0, which is standard but not guaranteed.
        # A more robust solution would find the interface first.
        list_cmd = subprocess.run(["networksetup", "-listpreferredwirelessnetworks", "en0"], 
                                  capture_output=True, text=True)
        
        if list_cmd.returncode != 0:
            print("Error listing Wi-Fi networks. Make sure Wi-Fi is enabled and interface is en0.")
            return

        lines = list_cmd.stdout.splitlines()
        # The first line is usually a header like "Preferred networks on en0:"
        # We skip it and any empty lines.
        ssids = [line.strip() for line in lines if line.strip() and not line.startswith("Preferred networks")]

        if not ssids:
            print("No saved Wi-Fi profiles found.")
            return

        if not ssids:
            print("No saved Wi-Fi profiles found.")
            return

        print(f"\nFound {len(ssids)} networks:")
        for i, ssid in enumerate(ssids, 1):
            print(f"{i}. {ssid}")

        print("\nEnter the number(s) of the network(s) you want to retrieve passwords for.")
        print("You can enter a single number (e.g. '5'), a range (e.g. '1-3'), comma-separated (e.g. '1, 5, 7'), or 'all'.")
        selection = input("Selection: ").strip().lower()

        selected_indices = set()
        if selection == 'all':
            selected_indices = set(range(1, len(ssids) + 1))
        else:
            parts = selection.split(',')
            for part in parts:
                part = part.strip()
                if '-' in part:
                    try:
                        start, end = map(int, part.split('-'))
                        selected_indices.update(range(start, end + 1))
                    except ValueError:
                        print(f"Invalid range: {part}")
                else:
                    try:
                        selected_indices.add(int(part))
                    except ValueError:
                        print(f"Invalid number: {part}")

        print(f"\nRetrieving passwords for {len(selected_indices)} networks (you may be prompted for Keychain access)...")

        for i in sorted(selected_indices):
            if 1 <= i <= len(ssids):
                ssid = ssids[i-1]
                try:
                    # Retrieve password from Keychain
                    cmd = ["security", "find-generic-password", "-wa", ssid]
                    
                    # If running as root, target the System keychain explicitly
                    if os.geteuid() == 0:
                        cmd.append("/Library/Keychains/System.keychain")

                    security_cmd = subprocess.run(cmd, capture_output=True, text=True)
                    
                    if security_cmd.returncode == 0:
                        password = security_cmd.stdout.strip()
                        print(f"WiFi Name: {ssid}, Password: {password}")
                    else:
                        print(f"WiFi Name: {ssid}, Password: [Could not retrieve - Keychain denied or not found]")
                
                except Exception as e:
                     print(f"WiFi Name: {ssid}, Error retrieving password: {e}")
            else:
                print(f"Skipping invalid index: {i}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    os_name = platform.system()
    print(f"Detected OS: {os_name}")
    
    if os_name == "Windows":
        get_windows_wifi_passwords()
    elif os_name == "Darwin": # macOS
        get_macos_wifi_passwords()
    else:
        print(f"Unsupported Operating System: {os_name}")

if __name__ == "__main__":
    main()
