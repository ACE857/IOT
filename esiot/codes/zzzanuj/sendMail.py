import smtplib
from email.mime.text import MIMEText

with open(textfile, 'rb') as fp:
    msg = MIMEText(fp.read())

me = 'anujsingh9710@gmail.com'# the sender's email address
you = 'nexsacramentum9710@gmail.com'# the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()