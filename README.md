# manage-your-mailbox

## Overview
`Manage Your Mailbox` is an automation tool that allows you to manage emails across multiple providers such as Gmail, Outlook and Yahoo by automating the transfer of emails from one account to another based on predefined criteria. This tool uses Python and interacts directly with email servers via IMAP and SMTP protocols.

## Features
- **Automatic Email Forwarding**: Automatically forwards emails from one account to another.
- **Support for Multiple Providers**: Works with Gmail, Outlook, and Yahoo.
- **Customizable Search Criteria**: Users can specify criteria such as unread emails to be transferred.
- **Secure Handling**: Uses secure connections for accessing and transferring emails.

## Prerequisites
Before using this tool, ensure you have:
- Python 3.x installed on your system.
- Access to the internet to connect to email servers.
- Permission to access IMAP and enable less secure apps on the email accounts you plan to manage.

## Variables

- row_number: la ligne du fichier "scrape mail.csv" correspondant au compte e-mail que vous souhaitez utiliser.
- SEARCH_CRITERIA: les critères de recherche utilisés pour récupérer les e-mails. Dans cet exemple, seuls les e-mails non lus sont transférés.
- FROM_ADDRESS: l'adresse e-mail que vous utilisez pour transférer les e-mails.
- TO_ADDRESS: l'adresse e-mail vers laquelle vous souhaitez transférer les e-mails.
- FORWARD_TIME_DELAY: le temps de retard entre chaque transfert d'e-mail.
- EXCEPTION_TIME_DELAY: le temps de pause entre chaque erreur de transfert d'e-mail.
- VERBOSE: un booléen qui indique si vous souhaitez afficher des informations détaillées sur le transfert des e-mails.

<p align="center">
  <img src="https://github.com/johannvig/manage-email/assets/102874093/7d1a69ff-8bdd-4693-b217-009a1cd45c97" width="500" alt="Screenshot 2024-04-30 201142">
</p>
<p align="center">
  <em>Picture 1: Homepage</em>
</p>

<p align="center">
  <img src="https://github.com/johannvig/manage-email/assets/102874093/97188aa8-8d57-41f5-ae26-5ca14ab30ad6" width="500" alt="Screenshot 2024-04-30 201142">
</p>

<p align="center">
  <em>Picture 2: Enter an option</em>
</p>

<p align="center">
  <img src="https://github.com/johannvig/manage-email/assets/102874093/a49bde4f-72fa-41f7-a08b-c57d995c09c6" width="500" alt="Screenshot 2024-04-30 201142">
</p>

<p align="center">
  <em>Picture 3: Enter an invalid option</em>
</p>



## Avertissements

Le script ne fonctionne qu'avec les fournisseurs de messagerie Gmail, Outlook et Yahoo.
Avant d'utiliser le script, vous devez activer l'IMAP et les applications moins sécurisées pour chaque e-mail que vous souhaitez utiliser avec cet outil.
Si vous souhaitez utiliser cet outil avec un autre fournisseur de boîte e-mail, vous devez rechercher le protocole IMAP et SMTP de ce fournisseur de boîte e-mail et remplacer "imap.gmail.com" par le nouveau.

