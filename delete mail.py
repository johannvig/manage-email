import imaplib
import email
from colorama import Fore
from csv import reader
import warnings

warnings.filterwarnings('ignore')


# WARNING: Active IMAP and less secure app before on every email you want to use with this script
# Note: The script can only be used with gmail, outlook and yahoo

def delete_mail():
    try:
        with open('','r') as csv_file:  # put the path of "delete mail.csv" file that you can download in the project (ex of a path: "../email/delete mail.csv")
            csv_reader = reader(csv_file)
            list_of_rows = list(csv_reader)

            row_number = s
            col_number = 1
            email_name = list_of_rows[row_number - 1][col_number - 1]

            # filter according to the type of email and uses the IMAP protocol associated with the type of email


            gmail = ["@gmail.com"]
            outlook = ["@outlook.com"]
            yahoo = ["@yahoo.com"]

            for imail in outlook:
                if imail in email_name:
                    mail = imaplib.IMAP4_SSL('imap-mail.outlook.com', 993)

            for imail in yahoo:
                if imail in email_name:
                    mail = imaplib.IMAP4_SSL('imap.mail.yahoo.com', 993)

            for imail in gmail:
                if imail in email_name:
                    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)


            # If you want to use this tool with another email box provider, you have to search the IMAP protocol of this email box provider and replace "imap.gmail.com" by the new one

            col_number = 2
            email_password = list_of_rows[row_number - 1][col_number - 1]

            mail.login(email_name, email_password)
            
            
            # select the mailbox you want to delete
            mail.select("inbox")      #you can use trash, draft, spam and sent to replace inbox
            
            
            # you can specify which email you want to delete by replace 'ALL' by 'FROM "username@emailprovider.com" if you want to delete mail from a specific person
            # Replace 'ALL' by 'SUBJECT "The Subject name"' if you want to delete mail from a specific subject
            # Replace 'ALL' by 'SINCE "01-JAN-2020"' if you want to delete mail from a specific date
            # or UNSEEN if you want to delete unread mail
            typ, data = mail.search(None, 'ALL') 
            
            
            # converting the messeges into specific ids
            for num in data[0].split():
                # deleting the mails
                mail.store(num, '+FLAGS', r'(\Deleted)')
                
                
            # parmanently deleting the mails that are selected
            mail.expunge()
            
            
            # closing the mailbox
            mail.close()
            
            # loging out form the mail id
            mail.logout()

    except Exception as e:
        print(Fore.RED + "Ohoh! Something went wrong! This email doesn't work:" + str(email_name))
        print(e)


k = "yes"
s = 2
while True:
    with open('', 'r') as csv_file: #put the path of "delete mail.csv" file that you can download in the project
        csv_reader = reader(csv_file)
        list_of_rows = list(csv_reader)
        # (list_of_rows)

        try:
            row_number = s
            col_number = 1
            value = list_of_rows[row_number - 1][col_number - 1]
        except:
            k = "no"

        if k == "no":
            print(Fore.GREEN + "program is over")
            print(Fore.GREEN + "Job done. Enjoy your day!")
            break


        else:
            delete_mail()
            s += 1
