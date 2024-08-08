import random
import smtplib
import schedule,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Read the file contents
with open("quotes.txt", "r") as f:
    content = f.read()

# Split the content into quotes using single newline as the delimiter
quotes = content.split("\n")

# Clean up the quotes (remove any extra whitespace and filter out empty strings)
quotes = [quote.strip() for quote in quotes if quote.strip()]




username = "rloveumom@gmail.com"
password = "pbjg bmgr uitp jnhr"

def sendMail():
    quote = random.choice(quotes)
    print(quote)
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = "rpranav1820@gmail.com"
    msg["From"] = username
    msg["Subject"] = "Daily Inspiration!"
    msg.attach(MIMEText(quote, "html"))

    s.send_message(msg)
    del msg

schedule.every(24).hours.do(sendMail)

while True:
    schedule.run_pending()
    time.sleep(1)


