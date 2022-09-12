# Python code to illustrate sending mail from your gmail account
import imp
import smtplib # cretes SMTP session
s = smtplib.SMTP('smtp.gmail.com',587) # start TLS for security
s.starttls() # Authentication
print("Login with your email id")
print("----------------------------------------------------------------------------------------")
print("Enter your email address:")
sen_mail = input() # Taking email id and password from the user 
print()
print("Enter your password: ")
password = input()
print()
try:
    s.login(sen_mail,password) #login in the user account
except:
    print("Enter correct email or password") # failed login condition
    print("------------------------------------------------------------------------------------------")
    quit()
print("Login Successful")
print("---------------------------------------------------------------------------------")
message = input("Enter the message that you want to send: \n") # Taking message from the user
print("")
rec_mail = input("Enter receivers Email adddress: \n") # Taking recievers email address
s.sendmail(sen_mail,rec_mail,message) # sending email
s.quit # Terminating the session