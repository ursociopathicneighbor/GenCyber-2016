import smtplib

to = 'anchang@cisco.com'

gmail_user = "pandacity@gmail.com"
gmail_pwd = "cedarw00d"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)

header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + "Subject: ANNOYING"
print(header)
msg = header + '\n DERRRRRRRRRRRRRRRRp\n\n'
smtpserver.sendmail(gmail_user, to, msg)
print('Done!')
smtpserver.close()

























