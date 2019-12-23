Sending Email Using Python
This program can sends email to multiple user. You need to input the email id of the users.

Run:
$ python mail.py

Output:
Sends email to user or multiple users.

$ python mail.py 
import smtplib 

s = smtplib.SMTP('smtp.gmail.com', 587) 
#Set up the SMTP server and log into your account.Put your host address and port

s.starttls()
#For security reasons, now put the SMTP connection in the TLS mode. TLS (Transport Layer Security) encrypts all the SMTP commands. 
	
s.login("sender_email_id", "password") 
#youremail address and password
 
s.quit
#is used to exit
