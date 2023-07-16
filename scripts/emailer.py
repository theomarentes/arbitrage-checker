import smtplib, ssl

class Emailer:
    def send_email(margin, high, high_exchange, low, low_exchange, sender, receiver, sender_password):
        port = 465  
        smtp_server = "smtp.gmail.com"
        sender_email = sender  
        receiver_email = receiver 
        password = sender_password
        message = f"""\
        From: Python

        Maximum: {high} at {high_exchange}
        Minimum: {low} at {low_exchange}
        Margin: {margin}%"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)