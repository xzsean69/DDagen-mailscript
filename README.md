# DDagen-mailscript

A Python script that sends emails automatically at 5-minute intervals using SMTP.

## Features

- Sends emails every 5 minutes
- Configurable SMTP settings via environment variables
- Support for TLS/SSL encryption
- Immediate email on startup
- Easy to configure and run

## Requirements

- Python 3.6 or higher
- SMTP server access (e.g., Gmail, Outlook, or custom SMTP server)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/xzsean69/DDagen-mailscript.git
cd DDagen-mailscript
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your email settings:
```bash
cp .env.example .env
```

4. Edit the `.env` file with your actual email credentials:
```bash
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
RECIPIENT_EMAIL=recipient@example.com
```

**Note for Gmail users:** You need to use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

## Usage

Run the script:
```bash
python send_mail.py
```

Or make it executable and run directly:
```bash
chmod +x send_mail.py
./send_mail.py
```

The script will:
1. Send an email immediately upon start
2. Continue sending emails every 5 minutes
3. Run until you stop it with `Ctrl+C`

## Configuration

The script uses the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `SMTP_SERVER` | SMTP server address | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP server port | `587` |
| `SENDER_EMAIL` | Your email address | (required) |
| `SENDER_PASSWORD` | Your email password/app password | (required) |
| `RECIPIENT_EMAIL` | Recipient email address | (required) |

## Security Notes

- Never commit your `.env` file with real credentials
- Use app-specific passwords when available
- Keep your credentials secure
- The `.gitignore` file is configured to exclude `.env`

## Troubleshooting

**Authentication Error:**
- For Gmail, make sure you're using an App Password, not your regular password
- Enable "Less secure app access" if using regular SMTP authentication (not recommended)

**Connection Error:**
- Check your SMTP server and port settings
- Ensure your firewall allows outbound connections on the SMTP port
- Verify your internet connection

**Missing Environment Variables:**
- Make sure your `.env` file is in the same directory as the script
- Ensure all required variables are set (SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)

## License

MIT