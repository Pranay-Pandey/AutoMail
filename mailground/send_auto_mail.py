# from message_to_send_copy import Mes
import smtplib, ssl, csv
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename
from email.mime.application import MIMEApplication
import json


sender = ''  #Type official-email
from_name_display = ''
password = ''       #Type App password of Python

# message_body_html = Mes.body_message()
# subject = "final_edit"
subject = ""


def send_email_pdf_figs(path_to_pdf=None):
    ## credits: http://linuxcursor.com/python-programming/06-how-to-send-pdf-ppt-attachment-with-html-body-in-python-script
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    i = 1
    with open(r'', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            receiver = row[0]
            # print(row[0])
            server.login(sender, password)
            # Craft message (obj)
            msg = MIMEMultipart()
            
            msg['Subject'] = subject
            msg['From'] = from_name_display
            msg['To'] = receiver
            # Insert the text to the msg going by e-mail
            msg.attach(MIMEText("message_body_html", "html"))
            # Attach the pdf to the msg going by e-mail
            if(path_to_pdf):
                with open(path_to_pdf, "rb") as f:
                    #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
                    attach = MIMEApplication(f.read(),_subtype="pdf")
                attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))
                msg.attach(attach)
            # send msg
            server.send_message(msg)
            print("Sent to ", receiver, f"{i}/59")
            i=i+1



def send_email(sender , sender_name ,password ,  receiver_email , subject, body , pdf_file=None):
    import smtplib, ssl, csv
    from email.message import EmailMessage
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from os.path import basename
    from email.mime.application import MIMEApplication
    import json
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    # Craft message (obj)
    msg = MIMEMultipart()
    
    msg['Subject'] = subject
    msg['From'] = sender_name
    msg['To'] = receiver_email
    # Insert the text to the msg going by e-mail
    msg.attach(MIMEText(body, "html"))
    # Attach the pdf to the msg going by e-mail
    if(pdf_file):
            #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
        attach = MIMEApplication(pdf_file.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str("attachment"))
        msg.attach(attach)
    # send msg
    server.send_message(msg)
    print("Sent to ", receiver_email)