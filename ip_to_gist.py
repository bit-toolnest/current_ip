import requests
import os

# === Replace these ===
GIST_ID = "FROM_GitHub"
FILENAME = "my-ip.txt"
GITHUB_TOKEN = "FROM GitHub"

# === Local RAM-backed file to store last known IP ===
STATE_FILE = "/dev/shm/last_ip.txt"

# === Get current IP ===
def get_public_ip():
    return requests.get("https://api.ipify.org").text.strip()

# === Read previous IP from /dev/shm ===
def get_previous_ip():
    if not os.path.exists(STATE_FILE):
        return None
    with open(STATE_FILE, "r") as f:
        return f.read().strip()

# === Save current IP to /dev/shm ===
def save_current_ip(ip):
    with open(STATE_FILE, "w") as f:
        f.write(ip)

# === Update the Gist ===
def update_gist(ip):
    url = f"https://api.github.com/gists/{GIST_ID}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    data = {
        "files": {
            FILENAME: {
                "content": ip
            }
        }
    }
    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Gist updated successfully.")
    else:
        print(f"Failed to update Gist: {response.status_code}")
        print(response.text)

# === Run it ===
if __name__ == "__main__":
    current_ip = get_public_ip()
    previous_ip = get_previous_ip()

    if previous_ip is None:
        print("No previous IP stored. Updating Gist...")
        update_gist(current_ip)
        save_current_ip(current_ip)
    elif current_ip != previous_ip:
        print(f"IP changed from {previous_ip} to {current_ip}. Updating Gist...")
        update_gist(current_ip)
        save_current_ip(current_ip)
    else:
        print("IP has not changed. No update needed.")

# Start this code on system boot and runs evey 5mins by
# open crone config: crontab -e
# Add this line: */5 * * * * /usr/bin/python3 /home/bitresearch/services/ip_to_gist.py
