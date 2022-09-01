import smtplib

msg = MIMEMultipart()
msg['From'] = 'aurelien640@live.fr'
msg['To'] = 'aureas640@live.fr'
msg['Subject'] = 'Le sujet de mon mail' 
message = 'Bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.live.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('aurelien640@live.com', 'Banane640')
mailserver.sendmail('aurelien640@live.com', 'aurelien640@live.com', msg.as_string())
mailserver.quit()
