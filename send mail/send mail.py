from colorama import Fore
from csv import reader
from random import randint
import smtplib
from discord_webhook import DiscordWebhook, DiscordEmbed
import warnings
from time import sleep

warnings.filterwarnings('ignore')

# WARNING: Active IMAP and less secure app before on every email you want to use with this script
# Note: The script can only be used with Gmail, Outlook, and Yahoo

def send_mail(row_number, file_path, webhook_url, discord_bot_name, discord_bot_icon):
    try:
        with open(file_path, 'r') as csv_file:  # path of "send mail.csv" file
            csv_reader = reader(csv_file)
            list_of_rows = list(csv_reader)

            col_number = 1
            email_name = list_of_rows[row_number - 1][col_number - 1]

            # filter according to the type of email and uses the SMTP protocol associated with the type of email
            gmail = ["@gmail.com"]
            outlook = ["@outlook.com"]
            yahoo = ["@yahoo.com"]

            smtpserver = None

            for email in outlook:
                if email in email_name:
                    smtpserver = smtplib.SMTP("smtp-mail.outlook.com", 587)  # use outlook with port

            for email in yahoo:
                if email in email_name:
                    smtpserver = smtplib.SMTP("smtp.mail.yahoo.com", 587)  # use yahoo with port

            for email in gmail:
                if email in email_name:
                    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port

            if smtpserver is None:
                print(Fore.RED + "No suitable SMTP server found for the email: " + email_name)
                return

            col_number = 2
            email_password = list_of_rows[row_number - 1][col_number - 1]

            col_number = 3
            email_receiver = list_of_rows[row_number - 1][col_number - 1]

            col_number = 4
            mail_subject = list_of_rows[row_number - 1][col_number - 1]

            col_number = 5
            mail_message = list_of_rows[row_number - 1][col_number - 1]

            # Create SMTP session for to send the mail
            smtpserver.ehlo()  # identify the computer system
            smtpserver.starttls()  # enable security

            # Log into the server
            smtpserver.login(email_name, email_password)

            # Send mail
            header = "To:" + email_receiver + "\n" + 'From: ' + email_name + '\n' + 'Subject:' + mail_subject + '\n'
            print(Fore.WHITE + header)
            msg = header + '\n ' + mail_message + ' \n\n'
            smtpserver.sendmail(email_name, email_receiver, msg)

            smtpserver.close()
            print(Fore.GREEN + 'Successfully sent')

            # Track all mail that you sent with a discord webhook
            webhook = DiscordWebhook(url=webhook_url)  # put your discord webhook url
            embed = DiscordEmbed(title="Task Success", color=3066993)
            embed.set_author(
                name=discord_bot_name,  # put the name of your discord bot
                icon_url=discord_bot_icon,  # put the profile image of your discord bot
            )
            embed.add_embed_field(name='Email', value=email_name, inline=False)
            embed.add_embed_field(name='Line of the CSV', value=row_number, inline=False)
            embed.add_embed_field(name='Tool', value="Send email", inline=False)
            webhook.add_embed(embed)
            embed.set_timestamp()
            response = webhook.execute(remove_embeds=True)

            g = randint(300, 600)
            v = g / 100
            sleep(v)
            print("Sleeping for " + str(v) + " seconds")
    except Exception as e:
        print(Fore.RED + "Ohoh! Something went wrong!")
        print(e)


if __name__ == "__main__":
    file_path = ''  # put the path of "send mail.csv" file
    webhook_url = ''  # put your discord webhook url
    discord_bot_name = ''  # put the name of your discord bot
    discord_bot_icon = ''  # put the profile image url of your discord bot

    k = "yes"
    s = 2
    while True:
        with open(file_path, 'r') as csv_file:  # path of "send mail.csv" file
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
                send_mail(row_number, file_path, webhook_url, discord_bot_name, discord_bot_icon)
                s += 1
