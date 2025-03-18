# 📌 Microsoft Teams Ticket Alert (Freshservice)

## 🎯 Overview
This script fetches tickets from **Freshservice** based on different statuses and sends notifications to **Microsoft Teams** via an Incoming Webhook. It helps IT teams track ticket updates efficiently.

## 🚀 Features
- Fetches tickets based on different statuses:
  - **Open (2)** → Current active tickets
  - **Pending (3)** → Tickets awaiting action
  - **Closed (5)** → Tickets closed in the last **7 days**
  - **In Progress (6)** → Ongoing work tickets
  - **Resolved (4)** → Resolved tickets in the last **7 days**
- Uses **`updated_at`** to fetch recent changes instead of `created_at`
- Groups tickets by assigned technician (`test_field`)
- Sends a **summary message** and **detailed ticket breakdown**
- Provides a **direct dashboard link** for further investigation
- **Handles errors gracefully**

## 🛠️ Setup & Installation
### 1️⃣ **Clone Repository**
```bash
git clone https://github.com/your-repo/msteams-ticket-alert.git
cd msteams-ticket-alert
```

### 2️⃣ **Install Dependencies**
```bash
pip install requests
```

### 3️⃣ **Set Environment Variables**
```bash
export FRESHSERVICE_API_KEY="your_freshservice_api_key"
export MSTEAMS_WEBHOOK_URL="your_teams_webhook_url"
```
_For Windows:_ Use `set` instead of `export`

### 4️⃣ **Run Script**
```bash
python MSTeamsTicketAlert.py
```

## ⏰ Automation Setup (GitHub Actions / Cron Job)
- To automate execution, you can schedule it to run **every 2 hours** (GitHub Actions / Cron Jobs / Task Scheduler)
- Example GitHub Actions workflow:
```yaml
on:
  schedule:
    - cron: '0 */2 * * *'  # Runs every 2 hours
```

## 📬 Sample Teams Notification Output
```
🎯 Ticket Status Summary
- Open: 3 ticket(s) (Present)
- Pending: 5 ticket(s) (Present)
- Closed: 10 ticket(s) (7 days)
- In Progress: 7 ticket(s) (Present)
- Resolved: 8 ticket(s) (7 days)

🚀 Tickets in Open
🔹 John Doe
  - ID: 12345 | Subject: Server Issue
  - ID: 12346 | Subject: Network Failure
🔹 Not Assign
  - ID: 12347 | Subject: Software Bug

🔗 **Access Dashboard (Incognito Mode):** [Click Here](https://itcentral.freshservice.com/a/dashboard/default)
```

## 📝 Recent Updates
- ✅ **Switched to `updated_at`** to fetch recent updates instead of created tickets
- ✅ **Fixed query encoding issues** using `urllib.parse.quote()`
- ✅ **Corrected `Resolved` status to 4 instead of 7**
- ✅ **Added Dashboard link for quick access**
- ✅ **Fixed unterminated string error in message formatting**

## 📄 License
MIT License - Modify and use freely.

🔹 **For any issues or improvements, feel free to contribute!** 🚀

