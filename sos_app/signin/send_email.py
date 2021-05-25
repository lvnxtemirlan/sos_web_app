import smtplib
from decouple import config
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
MY_ADDRESS = config("MY_ADDRESS")
MY_PASSWORD = config("MY_PASSWORD")
msg = MIMEMultipart()


def send_email(to_client, message, image_path):
    msg['From'] = MY_ADDRESS
    msg['To'] = to_client
    msg['Subject'] = Header('SAVE OUR SOULS QAZAQSTAN', 'utf-8').encode()
    # attache a MIMEText object to save email content
    msg_content = MIMEText(message, 'plain', 'utf-8')
    msg.attach(msg_content)
    # to add an attachment is just add a MIMEBase object to read a picture locally.
    with open(image_path, 'rb') as f:
        # set attachment mime and file name, the image type is png
        mime = MIMEBase('image', 'png', filename=image_path)
        # add required header data:
        mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
        mime.add_header('X-Attachment-Id', '0')
        mime.add_header('Content-ID', '<0>')
        # read attachment file content into the MIMEBase object
        mime.set_payload(f.read())
        # encode with base64
        encoders.encode_base64(mime)
        # add MIMEBase object to MIMEMultipart object
        msg.attach(mime)
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login(MY_ADDRESS, MY_PASSWORD)

    conn.sendmail(MY_ADDRESS, to_client, msg.as_string())
    conn.quit()

# send_email("ashimkhan.temirlan@gmail.com","<h2>dsafas</h2>dfasdfa", "/home/devtima/practice/sos_web_app/sos_app/media/1566974630169263977.webp")