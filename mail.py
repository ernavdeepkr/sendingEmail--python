#usr/bin
#sending email using python3

import smtplib 
# list of email_id to send the mail 
li = ["abc", "def", "xyz"] 

for i in range(len(li)): 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("x", "y") 
	message = "I m learning python so could u help me to continue further "
	s.sendmail("x", li[i], message)
    s.sendmail()
	s.quit()
