# 🚀 X-AutoPoster Bot

A universal, fully automated bot that posts scheduled content directly to X (formerly Twitter). Whether it's **Fitness Tips**, **Book Quotes**, or **Daily Code Challenges**, this bot handles the scheduling, formatting, and threading for you.

### ✨ Key Features

* **Universal Content Support:** Easily add any niche (Fitness, Cooking, Tech) via JSON.
* **Smart Chaining:** Automatically Quote-Tweets the previous post in a series to create visible, easy-to-follow threads.
* **Automated & Manual Triggers:** Runs on a precise schedule or via a manual "one-click" trigger with a category dropdown.
* **Zero Maintenance:** Powered by GitHub Actions—no servers, no databases, no costs.

---

## 🛠️ Prerequisites

1. An **X Developer Account** (Free or Basic tier).
2. A **GitHub Account**.
3. Python 3.12+ (Recommended).

---

## 🚀 Quick Start Guide

### 1. Clone & Prepare

```bash
git clone https://github.com/YOUR_USERNAME/X-AutoPoster-Bot.git
cd X-AutoPoster-Bot

```

### 2. Configure X API Permissions

1. Go to the [X Developer Portal](https://developer.x.com/en/portal/dashboard).
2. **App Settings:** Click the gear icon and set **User authentication settings** to **"Read and Write"**.
3. **Keys and Tokens:** Regenerate your **Access Token** and **Secret**. (Note: You must regenerate them *after* changing permissions to "Read and Write").

### 3. Setup GitHub Secrets & Permissions

To allow the bot to post and save its progress:

1. **Secrets:** Go to **Settings > Secrets and variables > Actions** and add:
* `TWITTER_API_KEY`, `TWITTER_API_SECRET`
* `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`


2. **Permissions:** Go to **Settings > Actions > General**, scroll to **Workflow permissions**, select **"Read and write permissions"**, and click **Save**.

---

## 📁 Project Structure

```text
├── .github/workflows/
│   └── post_scheduler.yml  # Automates the schedule & manual triggers
├── contents/               # Your JSON data files (e.g., fitness_tips.json)
├── modules/                # Custom formatters (e.g., fitness.py, quotes.py)
├── main.py                 # The core engine
├── poster.py               # Handles X API interaction
├── progress.json           # Stores Thread IDs to enable Quote-Tweets
└── requirements.txt        # Dependencies (tweepy, python-dotenv)

```

---

## 📝 Adding Your Own Content

### Step 1: Create a Content File

Create a new file in `contents/your_topic.json`:

```json
[
  {
    "count": 1,
    "topic": "The Perfect Squat",
    "body": "Keep your back straight and drive through your heels...",
    "next_post": true
  }
]

```

### Step 2: Create a Formatter

Create a file in `modules/your_topic.py` to define how your post looks:

```python
def format_my_topic(item):
    return f"🌟 {item['topic']}\n\n{item['body']}\n\n#Fitness"

```

### Step 3: Register in `main.py`

Add your new module to the `FORMATTERS` dictionary in `main.py`.

---

## ⏰ Scheduling

The bot is pre-configured to post twice a day. Edit `.github/workflows/post_scheduler.yml` to change the times:

* **Morning Post:** `0 8 * * *` (8:00 AM UTC)
* **Evening Post:** `0 20 * * *` (8:00 PM UTC)

---

## 🧪 Testing Locally

1. Install dependencies: `pip install -r requirements.txt`
2. Create a `.env` file with your X API keys.
3. Run: `python main.py fitness_tips`

---


---

## 1. What to edit in `main.py`

The `main.py` file is designed to be generic, but it needs to know about your custom "styling" (formatters).

### A. The Imports

If a user creates a new file called `modules/cooking.py`, they **must** import it at the top of `main.py`:

```python
# ADD THIS:
from modules.cooking import format_recipe 

```

### B. The `FORMATTERS` Dictionary

This is the "Brain" that connects the mode name to the styling function. If it’s not in this dictionary, the bot will use a basic, boring fallback style.

```python
FORMATTERS = {
    "fitness_tips": format_fitness,
    "book_quotes": format_quotes,
    "cooking": format_recipe  # <--- ADD THIS LINE
}

```

> **Rule:** The key `"cooking"` must match exactly the name of the JSON file in the contents folder (e.g., `contents/cooking.json`).

---

## 2. What to edit in the `.yml` file

The YAML file is the most important part for automation. If a user adds a new category, they need to update three places in the `.yml`.

### A. The `workflow_dispatch` (The Dropdown Menu)

This allows users to manually test their new category from the GitHub "Actions" tab.

```yaml
    inputs:
      mode:
        options:
          - fitness_tips
          - book_quotes
          - cooking  # <--- ADD YOUR NEW MODE HERE

```

### B. The `schedule` (The Clock)

GitHub uses UTC time. If a user wants a third post at midday, they add a new cron line.

```yaml
  schedule:
    - cron: '0 8 * * *'  # Morning
    - cron: '0 12 * * *' # ADDED: Midday Post
    - cron: '0 20 * * *' # Evening

```

### C. The `steps` (The Execution)

This is where you tell the bot *which* file to run at *which* time. You must add a new block for every scheduled time.

```yaml
      # Example: New Midday Post Step
      - name: Run Midday Post
        if: github.event.schedule == '0 12 * * *'
        run: python main.py cooking  # <--- Run the 'cooking' logic

```

---

## 3. Summary of the "Handoff"

To help you understand better, see this simple 3-step connection:

1. **Create Content:** Make `contents/art.json`.
2. **Create Formatter:** Make `modules/art.py` and link it in `main.py`'s `FORMATTERS`.
3. **Set Time:** Add the cron time and the `python main.py art` command to the `.yml`.

---

## 🤝 Contributing

Feel free to fork this repo and add new formatters or improved logic! Submit a PR with your changes.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed by [Kolardev]**

Would you like me to help you set up a **"Troubleshooting"** section for common errors like the 403 Forbidden or Git Push Rejections?