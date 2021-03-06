from colorama import Fore
from csv import reader
from random import randint
import smtplib
from discord_webhook import DiscordWebhook, DiscordEmbed
import warnings
from time import sleep

warnings.filterwarnings('ignore')


# WARNING: Active IMAP and less secure app before on every email you want to use with this script
# Note: The script can only be used with gmail, outlook and yahoo

def send_mail():

    try:
        with open('', 'r') as csv_file: #put the path of "send mail.csv" file that you can download in the project (ex of a path: "../email/send mail.csv")
            csv_reader = reader(csv_file)
            list_of_rows = list(csv_reader)

            row_number = s
            col_number = 1
            email_name = list_of_rows[row_number - 1][col_number - 1]

            # filter according to the type of email and uses the SMTP protocol associated with the type of email

            gmail = ["@gmail.com"]
            outlook = ["@outlook.com"]
            yahoo = ["@yahoo.com"]

            for email in outlook:
                if email in email_name:
                    smtpserver = smtplib.SMTP("smtp-mail.outlook.com", 587)  # use outlook with port

            for email in yahoo:
                if email in email_name:
                    smtpserver = smtplib.SMTP("smtp.mail.yahoo.com", 587)  # use yahoo with port

            for email in gmail:
                if email in email_name:
                    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port

            # If you want to use this tool with another email box provider, you have to search the SMTP protocol of this email box provider and replace "smtp.gmail.com" by the new one

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
            print(Fore.WHITE+header)
            msg = header + '\n ' + mail_message + ' \n\n'
            smtpserver.sendmail(email_name, email_receiver, msg)

            smtpserver.close()
            print(Fore.GREEN+'Successfully send')

            # Track all mail that you sent with a discord webhook

            webhook = DiscordWebhook(url="")  # put your discord webhook url
            embed = DiscordEmbed(title="task sucess", color=3066993)
            embed.set_author(
                name="",  # put the name of your discord bot
                icon_url="",  # put the profil image of your discord bot
            )
            embed.add_embed_field(name='email', value=email_name, inline=False)
            embed.add_embed_field(name='Line of the csv', value=s, inline=False)
            embed.add_embed_field(name='Tool', value="Send email", inline=False)
            webhook.add_embed(embed)
            embed.set_timestamp()
            response = webhook.execute(remove_embeds=True)

            g = randint(300, 600)
            v = g / 100
            sleep(v)
            print("sleep during " + str(v) + "seconde")
    except Exception as e:
        print(Fore.RED + "Ohoh! Something went wrong!")
        print(e)



k = "yes"
s = 2
while True:
    with open('', 'r') as csv_file: #put the path of "send mail.csv" file that you can download in the project  
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
            send_mail()
            s += 1
