# Slack Media Export
![License](https://img.shields.io/github/license/benmcnelly/Slack-Media-Export)
![Last Commit](https://img.shields.io/github/last-commit/benmcnelly/Slack-Media-Export)
![Contributors](https://img.shields.io/github/contributors/benmcnelly/Slack-Media-Export)
![Stars](https://img.shields.io/github/stars/benmcnelly/Slack-Media-Export?style=social)

A script for automatically downloading all media files from a Slack export.

## Overview

This script recursively scans through a Slack export folder, identifies media links in JSON files, and downloads the media files into a specified directory. It is designed to streamline the process of archiving media from Slack exports.

## Features
- Automatically processes JSON files in the provided directory.
- Recursively searches subdirectories for Slack export files.
- Downloads media files into a designated folder.
- Handles duplicate filenames by appending counters to avoid overwriting.
- Logs progress and errors into `process_log.txt`.

## Prerequisites
- Python 3.6+
- Required Python libraries: `requests`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/slack-media-export.git
   cd slack-media-export
   ```
2. Install the required Python library:
   ```bash
   pip install requests
   ```

## Quick Start
1. Place your extracted Slack export folder on your desktop or specify a custom location in the script.
2. By default, the script assumes the media token is embedded in the Slack export’s media URLs. If the token has expired, manually update the `SLACK_TOKEN` variable in the script.

   Example location setting for Windows (default):
   ```python
   backup_folder = os.path.join(os.path.expanduser("~"), "Desktop", "backup_folder")
   ```

3. For "Exiting Slack" exports, you can disable all users and make all channels public to ensure you have access to all data.

4. Run the script:
   ```bash
   python slack_export.py
   ```

5. Media files will be saved to the `media` folder in the current directory by default. Progress will be displayed in the CLI, and any errors will be logged in `process_log.txt`.

## Output Example
CLI output example:
```bash
Processing file: C:\Users\username\Desktop\backup_folder\xmas\2022-12-04.json
Downloaded: C:\Users\username\Desktop\backup_folder\media\christmas_float_ideas_2022.jpg
Processing file: C:\Users\username\Desktop\backup_folder\xmas\2022-12-05.json
Downloaded: C:\Users\username\Desktop\backup_folder\media\image.png_387
Process completed.
```

Log file (`process_log.txt`) example:
```
Processing file: C:\Users\username\Desktop\backup_folder\xmas\2022-12-04.json
Downloaded: C:\Users\username\Desktop\backup_folder\media\christmas_float_ideas_2022.jpg
Failed to download https://slack.com/files/abc123 (Status Code: 403)
```

## Configuration
- **SLACK_TOKEN**: Set the Slack token manually if needed.
- **MEDIA_DIR**: Adjust the output folder for downloaded media files.
- **LOG_FILE**: Customize the location of the log file if required.

## Known Limitations
- The script assumes that media links are stored under the `"url_private"` key in the JSON files.
- It does not currently support downloading from private channels requiring additional authentication.

## Contributing
Feel free to submit issues or pull requests to improve this script.

## License
This project is licensed under the Unlicense. See the LICENSE file for details.

## Disclaimer
Ensure you comply with Slack’s Terms of Service and your organization’s policies when using this script.
