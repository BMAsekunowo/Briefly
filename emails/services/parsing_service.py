from emails.utils.mock_inbox import get_mock_emails

def parse_user_inbox(user):
    print(f"📨 Parsing inbox for {user.username}...")
    emails = get_mock_emails(user.email)

    print(f"📨 Parsed {len(emails)} emails for {user.username} at {emails[0]['time']}")
    for email in emails:
        print(f"   - {email['subject']} from {email['from']}")
    
    return emails