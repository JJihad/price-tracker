import logging
import smtplib
from email.mime.text import MIMEText
from typing import List, Tuple
from models.item import Item

# Set the logging level & the log message format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def email_body(data: List[Tuple[Item, float, float]]) -> str:
    body = """Hi dear shopper,\n
    This is a sales alert for the following items :\n"""
    
    for item, previous_price, actual_price in data:
        body = body + f"""\n{item.label}
                       Previous price: {previous_price}
                       Actual price: {actual_price}
                       URL: {item.url}\n"""
        
    return body + '\n' + 'See you next time'

def send_email(subject, body, to_email):
    # Set up your email server and login details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'example@gmail.com'
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
