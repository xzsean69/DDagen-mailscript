#!/usr/bin/env python3
"""
Email sending script with 5-minute intervals.
Sends emails periodically using SMTP.
"""

import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import schedule


def send_email():
    """Send an email using SMTP configuration from environment variables."""
    # Get configuration from environment variables
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')
    
    # Validate required configuration
    if not sender_email or not sender_password or not recipient_email:
        print("ERROR: Missing required environment variables!")
        print("Please set: SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL")
        return False
    
    try:
        # Create message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = f"Scheduled Email - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        # Email body
        body = f"""
        This is an automated email sent at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.
        
        This email is part of a scheduled job that runs every 5 minutes.
        """
        
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable TLS encryption
            server.login(sender_email, sender_password)
            server.send_message(message)
        
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Email sent successfully to {recipient_email}")
        return True
        
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error sending email: {str(e)}")
        return False


def main():
    """Main function to schedule and run email sending."""
    print("Mail Script Started")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Sending emails every 5 minutes...")
    print("Press Ctrl+C to stop")
    print("=" * 50)
    
    # Schedule the email to be sent every 5 minutes
    schedule.every(5).minutes.do(send_email)
    
    # Send an email immediately on start
    send_email()
    
    # Keep the script running
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nMail script stopped by user")


if __name__ == "__main__":
    main()
