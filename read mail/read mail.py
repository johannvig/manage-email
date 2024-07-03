import imaplib
import email
from colorama import Fore
from csv import reader
from discord_webhook import DiscordWebhook, DiscordEmbed
import warnings

warnings.filterwarnings('ignore')


# WARNING: Active IMAP and less secure app before on every email you want to use with this script
# Note: The script can only be used with Gmail, Outlook, and Yahoo

def read_mail(row_number, file_path, webhook_url, discord_bot_name, discord_bot_icon):
    try:
        with open(file_path, 'r') as csv_file:  # path of "read mail.csv" file
            csv_reader = reader(csv_file)
            list_of_rows = list(csv_reader)

            col_number = 1
            email_name = list_of_rows[row_number - 1][col_number - 1]

            # filter according to the type of email and uses the IMAP protocol associated with the type of email
            gmail = ["@gmail.com"]
            outlook = ["@outlook.com"]
            yahoo = ["@yahoo.com"]

            host = None

            for imail in outlook:
                if imail in email_name:
                    host = 'imap-mail.outlook.com'

            for imail in yahoo:
                if imail in email_name:
                    host = 'imap.mail.yahoo.com'

            for imail in gmail:
                if imail in email_name:
                    host = 'imap.gmail.com'

            if host is None:
                print(Fore.RED + "No suitable mail server found for the email: " + email_name)
                return

            col_number = 2
            email_password = list_of_rows[row_number - 1][col_number - 1]

            col_number = 3
            email_sender = list_of_rows[row_number - 1][col_number - 1]

            # set connection
            mail = imaplib.IMAP4_SSL(host)

            # login
            mail.login(email_name, email_password)

            # select inbox
            mail.select("INBOX")

            # select specific mails
            _, selected_mails = mail.search(None, '(FROM "' + email_sender + '")')

            # total number of mails from specific user
            print("Total Messages from " + email_sender + ":", len(selected_mails[0].split()))

            for num in selected_mails[0].split():
                # take the text from the message
                _, data = mail.fetch(num, '(RFC822)')
                _, bytes_data = data[0]

                # convert the byte data to message to be readable
                email_message = email.message_from_bytes(bytes_data)
                print("\n===========================================")

                # access data
                print("Subject: ", email_message["subject"])
                print("To:", email_message["to"])
                print("From: ", email_message["from"])
                print("Date: ", email_message["date"])
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                        message = part.get_payload(decode=True)
                        print("Message: \n", message.decode())
                        print("==========================================\n")

                        # Track all mail that you sent with a discord webhook
                        webhook = DiscordWebhook(url=webhook_url)  # put your discord webhook url
                        embed = DiscordEmbed(title="Task Success", color=3066993)
                        embed.set_author(
                            name=discord_bot_name,  # put the name of your discord bot
                            icon_url=discord_bot_icon,  # put the profile image of your discord bot
                        )
                        embed.add_embed_field(name='Subject', value=email_message["subject"], inline=False)
                        embed.add_embed_field(name='To', value=email_message["to"], inline=False)
                        embed.add_embed_field(name='From', value=email_message["from"], inline=False)
                        embed.add_embed_field(name='Date', value=email_message["date"], inline=False)
                        embed.add_embed_field(name='Message', value=message.decode(), inline=False)
                        embed.add_embed_field(name='Email', value=email_name, inline=False)
                        embed.add_embed_field(name='Line of the CSV', value=row_number, inline=False)
                        embed.add_embed_field(name='Tool', value="Read mail", inline=False)
                        webhook.add_embed(embed)
                        embed.set_timestamp()
                        response = webhook.execute(remove_embeds=True)

                        break

    except Exception as e:
        print(Fore.RED + "Ohoh! Something went wrong! This email doesn't work:" + str(email_name))
        print(e)


if __name__ == "__main__":
    file_path = ''  # put the path of "read mail.csv" file
    webhook_url = ''  # put your discord webhook url
    discord_bot_name = ''  # put the name of your discord bot
    discord_bot_icon = ''  # put the profile image url of your discord bot

    k = "yes"
    s = 2
    while True:
        with open(file_path, 'r') as csv_file:  # path of "read mail.csv" file
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
                read_mail(row_number, file_path, webhook_url, discord_bot_name, discord_bot_icon)
                s += 1
