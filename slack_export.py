import os
import json
import requests
from urllib.parse import urlparse

# Replace this with your Slack token, only needed if your export doesn't have it included with the media 
SLACK_TOKEN = "your_slack_token_here"
MEDIA_DIR = os.path.join(os.getcwd(), "media")
LOG_FILE = os.path.join(os.getcwd(), "process_log.txt")

# Ensure output directories exist
os.makedirs(MEDIA_DIR, exist_ok=True)

def log_message(message):
    """Log messages to a file."""
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")
    print(message)

def download_file(url, output_dir):
    """Download a file from a Slack URL with authentication."""
    headers = {"Authorization": f"Bearer {SLACK_TOKEN}"}
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        file_path = os.path.join(output_dir, filename)
        
        # Handle duplicate files
        counter = 1
        while os.path.exists(file_path):
            file_path = os.path.join(output_dir, f"{filename}_{counter}")
            counter += 1

        # Write file to disk
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        log_message(f"Downloaded: {file_path}")
    else:
        log_message(f"Failed to download {url} (Status Code: {response.status_code})")

def process_json_files(json_dir, output_dir):
    """Recursively process JSON files and extract/download media URLs."""
    for root, _, files in os.walk(json_dir):
        for file in files:
            if file.endswith(".json"):
                filepath = os.path.join(root, file)
                log_message(f"Processing file: {filepath}")
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        for message in data:
                            if "files" in message:
                                for file_info in message["files"]:
                                    if "url_private" in file_info:
                                        download_file(file_info["url_private"], output_dir)
                except json.JSONDecodeError as e:
                    log_message(f"Failed to parse {filepath}: {str(e)}")
                except UnicodeDecodeError as e:
                    log_message(f"Failed to read {filepath} due to encoding issue: {str(e)}")


def main():
    backup_folder = os.path.join(os.path.expanduser("~"), "Desktop", "backup_folder")
    log_message(f"Starting process for folder: {backup_folder}")
    process_json_files(backup_folder, MEDIA_DIR)
    log_message("Process completed.")

if __name__ == "__main__":
    main()
