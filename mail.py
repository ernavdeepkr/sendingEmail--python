#!usr/bin/python
#sending email using python3

import smtplib 

# list of email_idof users to send the mail 
li = ["abc", "def", "xyz"] 

for i in range(len(li)): 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("sender_email_id", "password") 
	message = "I m learning python so could u help me to continue further "
	s.sendmail("sender_email_id", li[i], message)
    s.sendmail()
	s.quit()
