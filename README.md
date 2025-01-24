# Screenshot to Markdown Automator

If you are a student or a working professional who takes a lot of screenshots for note-taking, manually adding them to your markdown files can be tedious. This script automates the process by detecting new screenshots in a folder and appending them to a markdown file.

## Features
- Monitors a specified folder for new screenshots.
- Automatically appends image links to a markdown file.
- Supports `.png`, `.jpg`, and `.jpeg` formats.
- Runs in the background with minimal resource usage.

## How It Works
1. The script watches a folder for new image files.
2. When a new screenshot appears, it generates an `<img>` tag.
3. The tag is added to the markdown file, including a timestamp.
4. The process continues in a loop, checking for new screenshots every 30 seconds.

## Setup & Usage

### Requirements
- Python 3.x

### Configuration
Edit these variables in the script:
```python
screenshot_dir = "your_location"
markdown_file = "filename.md"      
```

### Running the Script
```sh
python screenshot_to_markdown.py
```
The script will start monitoring the folder. Press **Ctrl+C** to stop it.

## Code Overview

### Writing Image Tags to Markdown
```python
def write_img_tag_to_markdown(image_path):
```
- Creates an `<img>` tag with the screenshot path and timestamp.
- Appends the tag to the markdown file.

### Monitoring the Folder
```python
def monitor_screenshots():
```
- Checks the folder every 30 seconds for new images.
- If new files are found, it updates the markdown file.
