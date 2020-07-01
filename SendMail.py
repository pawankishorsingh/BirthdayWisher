# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage


def send_mail(server, send_from, send_to, subject, html_header, html_body, html_footer, imagePath, files=[], cc=[], bcc=[]):
    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = send_from
    msgRoot['To'] = send_to
    msgRoot['Cc'] = cc
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText(html_header+html_body+'<br><img src="cid:image1"><br>'+html_footer, 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open(imagePath, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    import smtplib
    smtp = smtplib.SMTP()
    smtp.connect(server)
    smtp.sendmail(send_from, send_to, msgRoot.as_string())
    smtp.quit()

if __name__ == "__main__":
    #TBD
    pass