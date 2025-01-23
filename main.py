import os
import time
from datetime import datetime

screenshot_dir = "your_location"
markdown_file = "filename.md" 

def write_img_tag_to_markdown(image_path):
    img_tag = (
        f'<img src="{image_path}" alt="Screenshot taken at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}" />\n'
        f'<br><br>\n'
    )
    with open(markdown_file, "a") as md_file:
        md_file.write(img_tag)
    print(f"Added {img_tag.strip()} to {markdown_file}")

def monitor_screenshots():
    print(f"Monitoring directory: {screenshot_dir}")
    print("Press Ctrl+C to stop.")
    
    before = set(os.listdir(screenshot_dir))
    
    while True:
        time.sleep(30)  #Check for new files 30 seconds
        after = set(os.listdir(screenshot_dir))
        added_files = after - before 
        if added_files:
            for file_name in added_files:
                if file_name.endswith((".png", ".jpg", ".jpeg")): 
                    image_path = os.path.join(screenshot_dir, file_name)
                    write_img_tag_to_markdown(image_path)
        before = after

if __name__ == "__main__":
    try:
        monitor_screenshots()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
