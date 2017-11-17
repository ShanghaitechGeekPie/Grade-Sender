#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
import time

# Config your send email
DEBUG = True
mail_user = "sender@example.edu.cn"
mail_pass = "YourPassword"
smtp_server = 'smtp.shanghaitech.edu.cn'
smtp_port = 25

# Config your mail template
title_template = '[{}] Your CS101 Final Exam Score'
content_template = '''
<table style="border-radius: 3px;border: 1px solid #d8d8d8;border-bottom-width: 2px;border-top-width: 0;width: 100%;">
	<tr style="border:0px;padding:0px;margin:0px;">
		<td style="padding:20px;text-align:center; background:#1C9EFF;color:white;padding:20px;">
			<h2 style="border:0px;padding:0px;margin:0px;">
				Your CS101 Final Exam Score
			</h2>
			<span>
				{}({})
			</span>
		</td>
	</tr>
	<tr style="border:0px;padding:0px;margin:0px;">
		<td style="padding:20px;">
			<p>
				Here is your final exam score:
			</p>
			<p>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>{} / 100</strong>
			</p>
			<p>
				Happy new year!
			</p>
		</td>
	</tr>
	<tr style="border:0px;padding:0px;margin:0px;">
		<td style="padding:20px;text-align:center;">
			<hr/>
			<p>
				Data Structures <small>(CS101)</small>, ShanghaiTech University
			</p>
		</td>
	</tr>
</table>
'''

def send(mail, name, id, score):
	msg = MIMEText(content_template.format(name, id, score), 'html')
	msg['From'] = mail_user
	msg['Subject'] = title_template.format(name)
	if DEBUG:
		msg['To'] = mail_user
	else:
		msg['To'] = mail
	server.send_message(msg)

# parse data file
print('Parsing data file ... ', end = '', flush = True)
try:
	file = open('grade.dat')
	lines = file.readlines()
	data = [i.split() for i in lines]
	file.close()
	print('Success! get {} data'.format(len(data)), flush = True)
except:
	print('Failed!', flush = True)
	exit(1)


# parse data file
print('Establish connection with server {}:{} ... '.format(smtp_server, smtp_port), end = '', flush = True)
try:
	server = smtplib.SMTP()
	server.connect(smtp_server, smtp_port)
	print('Success!', flush = True)
except:
	print('Failed!', flush = True)
	exit(1)

# parse data file
print('Login sender email {} ... '.format(mail_user), end = '', flush = True)
try:
	server.starttls()
	server.login(mail_user, mail_pass)
	print('Success!', flush = True)
except:
	server.quit()
	print('Failed!', flush = True)
	exit(1)

for i in range(len(data)):
	d = data[i]
	print('Sending: {} ... '.format(d[2]), end = '', flush = True)
	try:
		send(d[0], d[2], d[1], d[3])
		print('Success!', flush = True)
	except:
		server.quit()
		print('Failed!', flush = True)
		exit(1)
	if i % 5 == 4:
		server.quit()
		print('Waiting for timeout ... ', end = '', flush = True)
		time.sleep(65)
		print('Done.', flush = True)
		server.connect(smtp_server, smtp_port)
		# we are using TLS mathod
		server.starttls()
		server.login(mail_user,mail_pass)

server.quit()
