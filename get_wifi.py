import subprocess
import re


def get_wifi_passwords():
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


if __name__ == "__main__":
    get_wifi_passwords()
