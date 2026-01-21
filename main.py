import sys
import os
import json
from poster import XPoster
from utils import save_json, load_json

# Import your new generic modules here
from modules.fitness import format_fitness
from modules.quotes import format_quotes

# Updated FORMATTERS mapping using new examples
FORMATTERS = {
    "fitness_tips": format_fitness,      # e.g., "Part 001: The Perfect Squat"
    "book_quotes": format_quotes        # e.g., "Deep Work - Part 001"
} 

def load_progress():
    if not os.path.exists("progress.json"):
        # Create a default structure if file is missing
        return {}
    with open("progress.json", "r") as f:
        return json.load(f)
    
def find_and_update_next(content_list):
    for i, item in enumerate(content_list):
        if item.get("next_post") is True:
            item["next_post"] = False
            # If there's a next item, mark it. 
            # If not, maybe loop back to the start?
            if i + 1 < len(content_list):
                content_list[i + 1]["next_post"] = True
            else:
                print("🏁 Reached the end of the content list!")
            return item
    return None

def main():
    # 1. Flexible Input: Handle any mode name
    if len(sys.argv) < 2:
        print("Usage: python main.py [mode_name] (e.g., fitness_tips)")
        return

    mode = sys.argv[1].lower()
    bot = XPoster()
    
    # 2. Path Management: Using 'contents' folder
    file_path = f"contents/{mode}.json"
    
    if not os.path.exists(file_path):
        print(f"❌ Error: No content file found at {file_path}")
        return

    # 3. Load Progress & Content
    progress = load_progress() # Helper to ensure progress.json exists
    with open(file_path, "r") as f:
        content_list = json.load(f)

    # 4. Find the item marked 'next_post': true
    item = find_and_update_next(content_list)

    if item:
        # 5. Dynamic Formatting
        # If the user defined a specific formatter, use it. 
        # Otherwise, use a default fallback format.
        formatter = FORMATTERS.get(mode)
        if formatter:
            text = formatter(item)
        else:
            # Smart Fallback for public users
            title = item.get("title", mode.replace("_", " ").title())
            body = item.get("body", "")
            text = f"🌟 {title}\n\n{body}\n\n#AutomatedPost"

        # 6. Post and Chain (Quote Tweet)
        prev_id = progress.get(mode, {}).get("thread_id")
        new_id = bot.post(text, prev_id)
        
        if new_id:
            # Update state
            if mode not in progress:
                progress[mode] = {}
            progress[mode]["thread_id"] = new_id
            
            # Save everything
            save_json(file_path, content_list)
            save_json("progress.json", progress)
            print(f"✅ Posted to X: {mode}")