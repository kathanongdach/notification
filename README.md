# notification
# Freshservice Ticket Notification to Microsoft Teams

## 📌 Overview
This script is designed to fetch ticket details from Freshservice based on their statuses and send notifications to a Microsoft Teams channel via Webhook. It helps IT teams stay updated on open, pending, closed, and in-progress tickets, ensuring efficient ticket management.

## 🎯 Features
- Fetches tickets with statuses:
  - **Open (2)**
  - **Pending (3)**
  - **Closed (5)**
  - **In Progress (6)**
- Groups tickets by assigned technician (based on `test_field` in `custom_fields`).
- Sends formatted ticket details to a Microsoft Teams channel.
- Provides a summary of the number of tickets in each status.
- Handles empty or missing assigned technician fields by marking them as "Not Assign".

## 🛠️ Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- Freshservice API Key
- Microsoft Teams Webhook URL

## 🚀 Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/freshservice-msteams-notification.git
   cd freshservice-msteams-notification
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables:
   ```bash
   export FRESHSERVICE_API_KEY="your_freshservice_api_key"
   export MSTEAMS_WEBHOOK_URL="your_teams_webhook_url"
   ```
   *(For Windows, use `set` instead of `export`.)*

## 🔄 Usage
Run the script manually:
```bash
python MSTeamsTicketAlert.py
```

## ⏰ Automating Execution
To run the script automatically at specific times (e.g., 9:00 AM, 1:00 PM, 3:00 PM), you can:
- Use **Cron Jobs** (Linux/macOS)
- Use **Task Scheduler** (Windows)
- Deploy on a cloud platform with scheduled execution (GitHub Actions, AWS Lambda, etc.)

## 📬 Expected Output in Microsoft Teams
The script will send messages like this:
```
🎯 Ticket Status Summary
- Open: 5 ticket(s)
- Pending: 3 ticket(s)
- Closed: 10 ticket(s)
- In Progress: 2 ticket(s)

🚀 Tickets in Open
🔹 John Doe
  - ID: 12345 | Subject: Server Issue
  - ID: 12346 | Subject: Network Failure
---
🔹 Not Assign
  - ID: 12347 | Subject: Software Bug
---
```

## 📄 License
MIT License. Feel free to modify and use as needed.

