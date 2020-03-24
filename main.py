#!/usr/bin/python3

import sys
import smtplib

print('Triggering the python script')
print('Script name : ' + sys.argv[0])
if(len(sys.argv) < 2):
    print('No arguements passed to script')
else:
    # print ('Number of arguments:', len(sys.argv), 'arguments.')
    print('Script arguments : ' + sys.argv[0])
    print ('Argument List:', str(sys.argv[1:]))

sender_email = str(sys.argv[1])
password = str(sys.argv[2])
receiver_email = str(sys.argv[3])

# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(sender_email, password) 
  
# message to be sent 
message = "Hey there, Python script ran successfully inside the container"
  
# sending the mail 
s.sendmail(sender_email, receiver_email, message) 
  
# terminating the session 
s.quit() 