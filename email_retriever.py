import imaplib
import email
from email.header import decode_header
from training_model import categorize_email
from topic_classifier import predict_category
import os

EMAIL_HOST = "imap.gmail.com"
EMAIL_USER = "piraveendaya@gmail.com"
EMAIL_PASS = os.getenv('PASS')  # Use App Password if 2FA is enabled

mail = imaplib.IMAP4_SSL(EMAIL_HOST)
mail.login(EMAIL_USER, EMAIL_PASS)
mail.select("inbox")  # Select inbox

def get_emails():
    # Search for starred emails using Gmail's IMAP filter
    status, messages = mail.search(None, 'X-GM-RAW "is:starred"')

    email_ids = messages[0].split()

    return email_ids

def retrieve_n_emails(n, email_ids):    
    # Connect to Gmail IMAP
    ans = []
    for email_id in email_ids[-n:]:  # Change to fetch more
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        body = ""
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # Decode email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")

                # Get sender info
                sender = msg.get("From")

                # print(f"📩 Subject: {subject}")
                # print(f"📤 From: {sender}")

                # Extract email body
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        # Extract text from plain text emails
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            payload = part.get_payload(decode=True)
                            if payload:
                                body = payload.decode(errors="ignore")
                                #print(f"📜 Email Body: {body[:500]}...")  # Print first 500 characters
                                break  # Stop after finding the first valid text part
                else:
                    # Handle non-multipart emails
                    payload = msg.get_payload(decode=True)
                    if payload:
                        body = payload.decode(errors="ignore")
                        #print(f"📜 Email Body: {body[:500]}...")

                temp = categorize_email(body)
                if temp[0] == 'Positive':
                    temp = predict_category(body)
                ans.append({'sender': sender, 'subject': subject, 'body': body, 'category': temp[0]})
    return ans