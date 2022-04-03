import imaplib
import email
from colorama import Fore
from csv import reader
from discord_webhook import DiscordWebhook, DiscordEmbed
import warnings

warnings.filterwarnings('ignore')


# WARNING: Active IMAP and less secure app before on every email you want to use with this script
# Note: The script can only be used with gmail, outlook and yahoo

def read_mail():
    try:
        with open('','r') as csv_file:  # put the path of "read mail.csv" file that you can download in the project (ex of a path: "../email/read mail.csv")
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
                    host = 'imap-mail.outlook.com'

            for imail in yahoo:
                if imail in email_name:
                    host = 'imap.mail.yahoo.com'

            for imail in gmail:
                if imail in email_name:
                    host = 'imap.gmail.com'


            # If you want to use this tool with another email box provider, you have to search the IMAP protocol of this email box provider and replace "imap.gmail.com" by the new one

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
            _, selected_mails = mail.search(None, '(FROM "'+email_sender+'")')

            # total number of mails from specific user
            print("Total Messages from "+email_sender+":", len(selected_mails[0].split()))

            for num in selected_mails[0].split():
                #take the text from the message
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

                        webhook = DiscordWebhook(url="")  # put your discord webhook url
                        embed = DiscordEmbed(title="task sucess", color=3066993)
                        embed.set_author(
                            name="",  # put the name of your discord bot
                            icon_url="",  # put the profil image of your discord bot
                        )
                        embed.add_embed_field(name='Subject', value=email_message["subject"], inline=False)
                        embed.add_embed_field(name='To', value=email_message["to"], inline=False)
                        embed.add_embed_field(name='From', value=email_message["from"], inline=False)
                        embed.add_embed_field(name='Date', value=email_message["date"], inline=False)
                        embed.add_embed_field(name='Message', value=message.decode(), inline=False)
                        embed.add_embed_field(name='email', value=email_name, inline=False)
                        embed.add_embed_field(name='Line of the csv', value=s, inline=False)
                        embed.add_embed_field(name='Tool', value="Read mail", inline=False)
                        webhook.add_embed(embed)
                        embed.set_timestamp()
                        response = webhook.execute(remove_embeds=True)

                        break

    except Exception as e:
        print(Fore.RED + "Ohoh! Something went wrong! This email doesn't work:" + str(email_name))
        print(e)


k = "yes"
s = 2
while True:
    with open('', 'r') as csv_file: #put the path of "read mail.csv" file that you can download in the project
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
            read_mail()
            s += 1
