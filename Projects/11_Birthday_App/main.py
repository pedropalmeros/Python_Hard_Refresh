import smtplib
from email.message import EmailMessage


my_email = "palmeros.test@gmail.com"

try:
    with open("password.txt","r") as passfile:
        password = passfile.readline()
except FileNotFoundError:
        print("ERROR NO PASSWORD FILE")
        password = "NOT FOUND"
else: 
    print(password)

mail_message = """Subject:Hello\n\nThis is the body of my email"""


connection = smtplib.SMTP('smtp.gmail.com:587')
print("step 1")
connection.starttls()
connection.login(user=my_email, password = password)
connection.sendmail(from_addr=my_email, to_addrs="pedrofpalmeros@gmail.com", msg=mail_message)
connection.close()

