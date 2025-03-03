import requests
import json
import os
from collections import defaultdict
import base64

# --- Configuration ---
FRESHSERVICE_API_KEY = os.environ.get("FRESHSERVICE_API_KEY", "fOXn9aKFyCDjX53U4Ut")
FRESHSERVICE_URL = "https://itcentral.freshservice.com/api/v2/tickets/filter?workspace_id=4&query="
MSTEAMS_WEBHOOK_URL = os.environ.get("MSTEAMS_WEBHOOK_URL", "https://centralgroup.webhook.office.com/webhookb2/1708eb1d-ba35-4a83-b0a0-4df36322afc8@817e531d-191b-4cf5-8812-f0061d89b53d/IncomingWebhook/01b0f7c0209a4a23b873d1f1d7e4a60a/f146cef8-997f-4bc2-87db-fc4ae2bf4a1b/V2uN0Bkut7GG7MfHdeca86KOFfUJ9-StlTWQMg8swyuhI1")

# Encode API Key for Basic Authentication
encoded_api_key = base64.b64encode(f"{FRESHSERVICE_API_KEY}:X".encode()).decode()
HEADERS_FRESHSERVICE = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {encoded_api_key}"
}

HEADERS_TEAMS = {
    "Content-Type": "application/json"
}

# --- Functions ---
def get_tickets_by_status(status):
    """ดึงข้อมูล Ticket ตาม Status"""
    query = f'"status:{status}"'
    url = FRESHSERVICE_URL + query
    try:
        response = requests.get(url, headers=HEADERS_FRESHSERVICE)
        response.raise_for_status()
        data = response.json()
        return data.get("tickets", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching tickets for status {status}: {e}")
        return []

def send_teams_notification(message):
    """ส่งข้อความแจ้งเตือนเข้า Microsoft Teams"""
    payload = {"text": message}
    try:
        response = requests.post(MSTEAMS_WEBHOOK_URL, headers=HEADERS_TEAMS, json=payload)
        response.raise_for_status()
        print("Teams notification sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Teams notification: {e}")

def format_ticket_details(tickets, status_name):
    """จัดรูปแบบข้อความสำหรับ Microsoft Teams"""
    if not tickets:
        return f"**🚀 No tickets in {status_name}**"
    
    message = f"**🚀 Tickets in {status_name}**\n\n"
    assignee_tickets = defaultdict(list)

    for ticket in tickets:
        custom_fields = ticket.get("custom_fields") or {}  # ป้องกัน NoneType
        assignee = custom_fields.get("test_field", "") or "Not Assign"
        assignee = assignee.strip() if isinstance(assignee, str) else "Not Assign"
        assignee_tickets[assignee].append(ticket)
    
    for assignee, assigned_tickets in assignee_tickets.items():
        message += f"🔹 **{assignee}**\n"
        for ticket in assigned_tickets:
            message += f"  - **ID:** {ticket['id']} | **Subject:** {ticket['subject']}\n"
        message += "---\n"
    return message

def main():
    """ดึงข้อมูล Ticket และแจ้งเตือนเข้า Microsoft Teams"""
    statuses = {
        2: "Open",
        3: "Pending",
        5: "Closed",
        6: "In Progress"  # เพิ่ม Status ใหม่
    }
    
    summary_message = "**🎯 Ticket Status Summary**\n\n"
    
    for status, status_name in statuses.items():
        tickets = get_tickets_by_status(status)
        ticket_count = len(tickets)
        summary_message += f"- {status_name}: {ticket_count} ticket(s)\n"
        
        if ticket_count > 0:
            detail_message = format_ticket_details(tickets, status_name)
            send_teams_notification(detail_message)
    
    send_teams_notification(summary_message)

if __name__ == "__main__":
    main()
