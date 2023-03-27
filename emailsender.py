import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv


email_addr = 'example@gmail.com'
email_pass = 'password'
email_sndr = 'Danish Sharjeel <example@gmail.com>'

with open('emails_list.csv') as file:
    reader = csv.reader(file)         # Containing list of emails
    next(reader)
    for comp_name, email_recr in reader:
        email_subj = 'Email Subject'  # Enter your email subject here

        # Email body
        email_body = f"""<p style="font-size:16px;">Greetings,
         <br/><br/>
         Your Email {comp_name}
        <br/><br/>
        With best regards,<br/>
        Danish Sharjeel
        </p>
        """
        
        send_email = MIMEMultipart()
        send_email["From"] = email_sndr
        send_email["To"] = email_recr
        send_email["Subject"] = email_subj
        send_email.attach(MIMEText(email_body, 'html'))

        email_attachment = open('image.jpg', 'rb')
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(email_attachment.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment; filename=image.jpg')
        send_email.attach(attachment)

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(email_addr, email_pass)

        textwrap = send_email.as_string()
        server.sendmail(email_sndr, email_recr, textwrap)

        print(f'Sent to {comp_name} at {email_recr}')

server.quit()
