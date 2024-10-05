import logging
import smtplib
from email.mime.text import MIMEText

# Set the logging level & the log message format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def email_body(url: str, previous_price: float, actual_price: float) -> str:
    return f"""Hi,
     Price drop of item in {url}.
     Previous price is : ${previous_price}.
     Actual price is : ${actual_price}."""

def send_email(subject, body, to_email):
    # Set up your email server and login details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'jbr.jihad@gmail.com'
    password = 'rpmm yojt ipyz irtw'

    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

# Example usage
#send_email("Test Alert", "This is a test alert from Python.", "recipient_email@example.com")
