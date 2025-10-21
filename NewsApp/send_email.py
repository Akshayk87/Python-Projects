
import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "akshaykunnath84@gmail.com"
    password = "qmfn brlm hdly ljrs"  # Use an app password for better security

    receiver = "akshayk8714@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

send_email("Hello, this is a test email from the NewsApp!")