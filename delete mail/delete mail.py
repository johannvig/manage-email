import imaplib
import email
from colorama import Fore
from csv import reader
import warnings

warnings.filterwarnings('ignore')


# WARNING: Active IMAP and less secure app before on every email you want to use with this script
# Note: The script can only be used with Gmail, Outlook, and Yahoo

def delete_mail(row_number, file_path):
    print("Deleting mail...")

    try:
        with open(file_path, 'r') as csv_file:  # path of "delete mail.csv" file
            csv_reader = reader(csv_file)
            list_of_rows = list(csv_reader)

            col_number = 1
            email_name = list_of_rows[row_number - 1][col_number - 1]

            # filter according to the type of email and uses the IMAP protocol associated with the type of email
            gmail = ["@gmail.com"]
            outlook = ["@outlook.com"]
            yahoo = ["@yahoo.com"]

            mail = None

            for imail in outlook:
                if imail in email_name:
                    mail = imaplib.IMAP4_SSL('imap-mail.outlook.com', 993)

            for imail in yahoo:
                if imail in email_name:
                    mail = imaplib.IMAP4_SSL('imap.mail.yahoo.com', 993)

            for imail in gmail:
                if imail in email_name:
                    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)

            if mail is None:
                print(Fore.RED + "No suitable mail server found for the email: " + email_name)
                return

            col_number = 2
            email_password = list_of_rows[row_number - 1][col_number - 1]

            mail.login(email_name, email_password)
            
            # Select the mailbox you want to delete
            mail.select("inbox")  # you can use trash, draft, spam, and sent to replace inbox
            
            # Specify which email you want to delete
            typ, data = mail.search(None, 'ALL') 
            
            # Converting the messages into specific ids
            for num in data[0].split():
                # Deleting the mails
                mail.store(num, '+FLAGS', r'(\Deleted)')
                
            # Permanently deleting the mails that are selected
            mail.expunge()
            
            # Closing the mailbox
            mail.close()
            
            # Logging out from the mail id
            mail.logout()

    except Exception as e:
        print(Fore.RED + "Ohoh! Something went wrong! This email doesn't work:" + str(email_name))
        print(e)

if __name__ == "__main__":
    file_path = ''  # put the path of "delete mail.csv" file that you can download in the project
    k = "yes"
    s = 2
    while True:
        with open(file_path, 'r') as csv_file:  # path of "delete mail.csv" file
            csv_reader = reader(csv_file)
            list_of_rows = list(csv_reader)

            try:
                row_number = s
                col_number = 1
                value = list_of_rows[row_number - 1][col_number - 1]
            except IndexError:
                k = "no"

            if k == "no":
                print(Fore.GREEN + "Program is over")
                print(Fore.GREEN + "Job done. Enjoy your day!")
                break
            else:
                delete_mail(row_number, file_path)
                s += 1
