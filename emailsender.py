import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv


email_addr = 'danishsharjeel3@gmail.com'
email_pass = 'Aw{VBU&d@Vq&g#1Nu0k'
email_sndr = 'Danish Sharjeel <danishsharjeel3@gmail.com>'

# email_recr = 'danishsharjeel7@gmail.com'
# comp_name = 'CoderHogwarts'
# comp_link = 'coderhogwarts.com'

with open('emails_data.csv') as file:
    reader = csv.reader(file)
    next(reader)
    for comp_name, comp_link, email_recr in reader:
        email_subj = 'Email Subject'  #Enter your email subject here

        # Email body for data science intrn
        email_body = f"""<p style="font-size:16px;">Respected Sir/Ma’am,
         <br/><br/>
        Most humbly, I am writing this email concerning the available opportunity for a remote internship at {comp_name}.
        My name is Danish Sharjeel and I am a first-year student of BS Computer Science. I recently started looking for
        Data Analyst internships and saw your company website {comp_link} listed as a Big Data/AI solution tech company hence I'm
        emailing for an open opportunity as Remote Data Science Intern.
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

        email_attachment = open('Resume.pdf', 'rb')
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(email_attachment.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment; filename=Resume.pdf')
        send_email.attach(attachment)

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(email_addr, email_pass)

        textwrap = send_email.as_string()
        server.sendmail(email_sndr, email_recr, textwrap)

        print(f'Sent to {comp_name} at {email_recr}')

server.quit()
