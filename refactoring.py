import email
import smtplib
import imaplib
# from email.MIMEText import MIMEText
# from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Gmail:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"
    recipients = ['vasya@email.com', 'petya@email.com']
    send_session = smtplib.SMTP(GMAIL_SMTP, 587)
    send_session.ehlo()
    send_session.starttls()
    send_session.ehlo()
    mail = imaplib.IMAP4_SSL(GMAIL_IMAP)

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message(self, subject: str, text_message: str):
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(self.recipients)
        message['Subject'] = subject
        message.attach(MIMEText(text_message))
        self.send_session.login(self.login, self.password)
        # self.send_session.sendmail(self.login, self.send_session, message.as_string())
        self.send_session.sendmail(self.login, self.recipients, message.as_string())
        self.send_session.quit()

    def receive_messages(self, header=None):
        self.mail.login(self.login, self.password)
        self.mail.list()
        self.mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = self.mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = self.mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        self.mail.logout()


if __name__ == '__main__':
    gmail = Gmail(input('login:'), input('password:'))
    gmail.send_message('subject', 'text message')
    gmail.receive_messages()
