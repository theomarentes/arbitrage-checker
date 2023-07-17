from scripts.logic import Logic


# Enter your email username (must be gmail)
sender_email = ""

# Enter your gmail app-specific password
sender_password = ""

# Enter notification receiving email address
receiver_email = ""

# Enter the margin required to send an email (in percent)
email_margin = 1


Logic.logic(email_margin, sender_email, receiver_email, sender_password)