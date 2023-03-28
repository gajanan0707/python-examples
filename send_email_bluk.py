'''
This Python code is used to send emails in bulk to a list of recipients, read from a CSV file. Here is a step-by-step explanation of the code:

The first few lines of the code define the email account details, such as the email address and password, which are used to log in to the SMTP server.
The SMTP server details, such as server name and port number, are also defined.
The smtplib library is then used to set up an SMTP server connection with the server name and port number defined earlier. The starttls() method is called to start a secure TLS connection with the server.
The login() method is used to log in to the email account using the email address and password provided earlier.
The code then reads data from a CSV file, named emails.csv. This file is assumed to have three columns: recipient email address, subject, and body of the email message.
The csv.reader method is used to read the data from the CSV file.
A for loop is then used to iterate through each row of the CSV file and extract the email details for each recipient.
The extracted email details are then used to create an email message using the message variable.
Finally, the server.sendmail() method is used to send the email message to the recipient email address.
After sending the email to all recipients, the server.quit() method is called to close the SMTP server connection.
Note that this code assumes that the CSV file is located in the same directory as the Python script and is named emails.csv. Also, the CSV file must have a header row with the column names Email, Subject, and Body. If your CSV file has different column names, you will need to modify the code to match your CSV file's column names.

'''
import smtplib
import csv

# Enter your email details
email = "your_email@example.com"
password = "your_email_password"

# Set up the SMTP server
smtp_server = "smtp.example.com"
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email, password)

# Read data from CSV file
with open("emails.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # Get email details from CSV row
        recipient_email = row[0]
        subject = row[1]
        body = row[2]

        # Create email message
        message = f"Subject: {subject}\n\n{body}"

        # Send email
        server.sendmail(email, recipient_email, message)

# Close the SMTP server connection
server.quit()
