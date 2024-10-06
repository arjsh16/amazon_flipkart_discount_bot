#to understand this code go to my other repository 
from email.message import EmailMessage
import ssl
import smtplib

def send_mail(receive_email,book_link,current_price):
    email_sender=''
    email_password='' 
    email_reciever=receive_email

    subject=f"Item status update"
    body=f"\nYour item \n{book_link}\n is now available at {current_price}% discount.\n"

    em=EmailMessage()

    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context=ssl.create_default_context()
    #smtp:simple mail transfer protocol
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciever,em.as_string())
import email.message
import ssl
import smtplib

def send_mail(recipient_email, book_link, current_price):
    """Sends an email notification when a book becomes available at a discount.

    Args:
        recipient_email (str): The email address of the recipient.
        book_link (str): The URL of the book page.
        current_price (float or int): The current discounted price of the book.

    Raises:
        smtplib.SMTPException: If an error occurs during the email sending process.
    """

    # Replace with your actual email credentials (avoid storing them in code)
    sender_email = "your_email@example.com"
    sender_password = "your_password"
  
    subject = f"Item Status Update: {book_link} Now Available at {current_price}% Discount!"
    body = f"\nYour desired item:\n{book_link}\n is now available at a discount of {current_price}%.\n"

    message = email.message.EmailMessage()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Error sending email:", e)
