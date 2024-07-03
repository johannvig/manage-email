import imaplib
import email
import smtplib
import time
from colorama import Fore
from csv import reader
from discord_webhook import DiscordWebhook, DiscordEmbed
import warnings

warnings.filterwarnings('ignore')


# WARNING: Active IMAP and less secure app before on every email you want to use with this script
# Note: The script can only be used with Gmail, Outlook, and Yahoo

def scrape_mail(row_number, file_path):
    try:
        with open(file_path, 'r') as csv_file:  # path of "scrape mail.csv" file
            csv_reader = reader(csv_file)
            list_of_rows = list(csv_reader)

            col_number = 1
            USERNAME = list_of_rows[row_number - 1][col_number - 1]

            # filter according to the type of email and uses the IMAP protocol associated with the type of email
            gmail = ["@gmail.com"]
            outlook = ["@outlook.com"]
            yahoo = ["@yahoo.com"]

            IMAP_HOST = None
            smtpserver = None

            for imail in outlook:
                if imail in USERNAME:
                    IMAP_HOST = 'imap-mail.outlook.com'
                    smtpserver = "smtp-mail.outlook.com"

            for imail in yahoo:
                if imail in USERNAME:
                    IMAP_HOST = 'imap.mail.yahoo.com'
                    smtpserver = "smtp.mail.yahoo.com"

            for imail in gmail:
                if imail in USERNAME:
                    IMAP_HOST = 'imap.gmail.com'
                    smtpserver = "smtp.gmail.com"

            if IMAP_HOST is None or smtpserver is None:
                print(Fore.RED + "No suitable mail server found for the email: " + USERNAME)
                return

            col_number = 2
            PASSWORD = list_of_rows[row_number - 1][col_number - 1]

            col_number = 3
            TO_ADDRESS = list_of_rows[row_number - 1][col_number - 1]

            SEARCH_CRITERIA = "UNSEEN"
            FROM_ADDRESS = USERNAME

            FORWARD_TIME_DELAY = 5
            EXCEPTION_TIME_DELAY = 60
            VERBOSE = True

            # Open IMAP connection
            imap_client = imaplib.IMAP4_SSL(IMAP_HOST, 993)
            imap_client.login(USERNAME, PASSWORD)

            # Fetch messages' ID list
            status, _ = imap_client.select("INBOX", readonly=True)
            if status != "OK":
                raise Exception("Could not select connect to INBOX.")

            status, data = imap_client.search(None, SEARCH_CRITERIA)
            if status != "OK":
                raise Exception("Could not search for emails.")

            messages_id_list = data[0].decode("utf-8").split(' ')
            if VERBOSE:
                print(
                    "{} messages were found. Forwarding will start immediately.".format(len(messages_id_list)))
                print("Messages ids: {}".format(messages_id_list))
                print()

            # Fetch each message data
            messages_sent = []
            while len(messages_sent) < len(messages_id_list):
                msg_id = messages_id_list[len(messages_sent)]

                status, msg_data = imap_client.fetch(msg_id, '(RFC822)')
                if status != "OK":
                    raise Exception("Could not fetch email with id {}".format(msg_id))

                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])

                        # Change FROM and TO header of the message
                        msg.replace_header("From", FROM_ADDRESS)
                        msg.replace_header("To", TO_ADDRESS)

                        try:
                            # Open SMTP connection
                            smtp_client = smtplib.SMTP(smtpserver, 587)
                            smtp_client.starttls()
                            smtp_client.ehlo()
                            smtp_client.login(USERNAME, PASSWORD)

                            # Send message
                            smtp_client.sendmail(FROM_ADDRESS, TO_ADDRESS, msg.as_bytes())
                            messages_sent.append(msg_id)
                            if VERBOSE:
                                print("Message {} was sent. {} emails from {} emails were forwarded.".format(
                                    msg_id,
                                    len(messages_sent),
                                    len(messages_id_list)))

                            # Close SMTP connection
                            smtp_client.close()

                            # Time delay until next command
                            time.sleep(FORWARD_TIME_DELAY)
                        except smtplib.SMTPSenderRefused as exception:
                            if VERBOSE:
                                print("Encountered an error! Error: {}".format(exception))
                                print("Messages sent until now:")
                                print(messages_sent)
                                print("Time to take a break. Will start again in {} seconds.".format(
                                    EXCEPTION_TIME_DELAY))
                            time.sleep(EXCEPTION_TIME_DELAY)
                        except smtplib.SMTPServerDisconnected as exception:
                            if VERBOSE:
                                print("Server disconnected: {}".format(exception))
                        except smtplib.SMTPNotSupportedError as exception:
                            if VERBOSE:
                                print("Connection failed: {}".format(exception))
                                print("Messages sent until now:")
                                print(messages_sent)
                                print("Time to take a break. Will start again in {} seconds.".format(EXCEPTION_TIME_DELAY))
                            time.sleep(EXCEPTION_TIME_DELAY)
                        except smtplib.SMTPDataError:
                            raise Exception("Daily user sending quota exceeded.")

            if VERBOSE:
                print("Job done. Enjoy your day!")

            # Logout
            imap_client.close()
            imap_client.logout()

    except Exception as e:
        print(Fore.RED + "Ohoh! Something went wrong! This email doesn't work:" + str(USERNAME))
        print(e)


if __name__ == "__main__":
    file_path = ''  # put the path of "scrape mail.csv" file

    k = "yes"
    s = 2
    while True:
        with open(file_path, 'r') as csv_file:  # path of "scrape mail.csv" file
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
                scrape_mail(row_number, file_path)
                s += 1
