import sys
import json
from poster import XPoster
from modules.designer import format_system_design
from modules.coder import format_leetcode
from modules.fact_checker import format_tech_fact

def find_and_update_next(content_list):
    for i, item in enumerate(content_list):
        if item.get("next_post") == True:
            item["next_post"] = False
            if i + 1 < len(content_list):
                content_list[i + 1]["next_post"] = True
            return item
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [system_design | leetcode | tech_facts]")
        return

    mode = sys.argv[1]
    bot = XPoster()

    try:
        with open("progress.json", "r") as f:
            progress = json.load(f)
    except FileNotFoundError:
        print("Error: progress.json not found.")
        return

    # --- AUTOMATED MODES ---
    if mode in ["system_design", "tech_facts"]:
        file_path = f"content/{mode}.json"
        with open(file_path, "r") as f:
            content = json.load(f)
        
        item = find_and_update_next(content)

        if item:
            if mode == "system_design":
                text = format_system_design(item)
            else:
                text = format_tech_fact(item)

            tid = bot.post(text, progress[mode]["thread_id"])
            
            if tid:
                progress[mode]["thread_id"] = tid
                # Write changes back to the JSON content file (the True/False flip)
                with open(file_path, "w") as f:
                    json.dump(content, f, indent=2)

    # --- MANUAL MODE ---
    elif mode == "leetcode":
        name = input("Problem Name: ")
        url = input("Gist URL: ")
        day = progress["leetcode"]["day"] + 1
        text = format_leetcode(name, url, day)
        
        tid = bot.post(text, progress[mode]["thread_id"])
        if tid:
            progress["leetcode"]["day"] = day
            progress["leetcode"]["thread_id"] = tid

    # Save Progress
    with open("progress.json", "w") as f:
        json.dump(progress, f, indent=2)

if __name__ == "__main__":
    main()