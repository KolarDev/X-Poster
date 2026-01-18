# 🚀 X-AutoLearning: Daily Tech Automation Bot

A fully automated "Learning-in-Public" bot that posts daily **System Design** insights and **Tech Facts** directly to X (formerly Twitter). No hosting costs, no servers—just GitHub Actions and pure Python.

### ✨ Key Features

* **Automated Scheduling:** Posts every morning (System Design) and evening (Tech Facts).
* **Quote-Tweet Logic:** Automatically chains daily posts together via Quote Retweets to build a visible learning history.
* **Stateful Memory:** Uses a `progress.json` file to track threads and pointers.
* **Zero Cost:** Runs entirely on the GitHub Free Tier.

---

## 🛠️ Prerequisites

Before you begin, you will need:

1. An **X Developer Account** (Free or Basic tier).
2. A **GitHub Account**.
3. Python 3.9+ installed locally.

---

## 🚀 Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name

```

### 2. Configure X API Keys

You must enable **Read and Write** permissions on your X App.

1. Go to the [X Developer Portal](https://developer.x.com/en/portal/dashboard).
2. **App Settings:** Set User Authentication to **"Read and Write"**.
3. **Keys and Tokens:** Regenerate and save the following:
* `API Key` & `API Key Secret` (Consumer Keys)
* `Access Token` & `Access Token Secret`
* `Bearer Token`



### 3. Setup GitHub Secrets

To keep your keys safe, do **not** hardcode them. Add them as Repository Secrets:

1. Navigate to your repo on GitHub: **Settings > Secrets and variables > Actions**.
2. Add a **New repository secret** for each:
* `TWITTER_API_KEY`
* `TWITTER_API_SECRET`
* `TWITTER_ACCESS_TOKEN`
* `TWITTER_ACCESS_TOKEN_SECRET`
* `TWITTER_BEARER_TOKEN`



### 4. Enable Workflow Permissions

For the bot to save its progress back to GitHub:

1. Go to **Settings > Actions > General**.
2. Change **Workflow permissions** to **"Read and write permissions"**.
3. Click **Save**.

---

## 📁 Project Structure

```text
├── .github/workflows/
│   └── post_scheduler.yml  # The "brain" that runs the schedule
├── content/
│   ├── system_design.json  # Your library of system design posts
│   └── tech_facts.json     # Your library of fun tech facts
├── modules/
│   ├── designer.py         # Formatter for System Design posts
│   ├── fact_checker.py     # Formatter for Tech Facts
│   └── coder.py            # Formatter for LeetCode posts
├── main.py                 # Core logic and file handling
├── poster.py               # Tweepy wrapper for X API
├── progress.json           # Tracks current thread IDs and status
└── requirements.txt        # Python dependencies

```

---

## 📝 Customizing Content

### Adding Posts

Open `content/system_design.json`. Add your objects following this structure:

```json
{
  "count": 1,
  "topic": "Load Balancers",
  "body": "Your punchy explanation here...",
  "tags": "#SystemDesign #Tech",
  "next_post": true
}

```

> **Note:** Ensure only **one** item has `"next_post": true`. The bot will automatically move this flag to the next item after posting.

### Changing the Schedule

The bot uses **GitHub Actions Cron Syntax**. Edit `.github/workflows/post_scheduler.yml`:

* Morning Post: `0 8 * * *` (8:00 AM UTC)
* Evening Post: `0 20 * * *` (8:00 PM UTC)

---

## 🧪 Testing Locally

1. Install dependencies:
```bash
pip install -r requirements.txt

```


2. Create a `.env` file with your keys.
3. Run the script for a specific mode:
```bash
python main.py system_design

```



---

## 🤝 Contributing

Contributions are welcome! If you have better content or more advanced system design topics, feel free to fork the repo and submit a PR.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Made with ❤️ by [Your Name]**

Would you like me to also generate a `LICENSE` file text for you to include in the repo?