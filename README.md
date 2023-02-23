# manage-your-mailbox


Un outil Python pour faire gérer automatiquement les e-mails à partir d'un compte Gmail, Outlook ou Yahoo vers un autre compte e-mail spécifié.

Comment utiliser l'outil

Clonez le référentiel ou téléchargez le code source.
Installez les dépendances nécessaires via pip install -r requirements.txt.


Variables

row_number: la ligne du fichier "scrape mail.csv" correspondant au compte e-mail que vous souhaitez utiliser.
SEARCH_CRITERIA: les critères de recherche utilisés pour récupérer les e-mails. Dans cet exemple, seuls les e-mails non lus sont transférés.
FROM_ADDRESS: l'adresse e-mail que vous utilisez pour transférer les e-mails.
TO_ADDRESS: l'adresse e-mail vers laquelle vous souhaitez transférer les e-mails.
FORWARD_TIME_DELAY: le temps de retard entre chaque transfert d'e-mail.
EXCEPTION_TIME_DELAY: le temps de pause entre chaque erreur de transfert d'e-mail.
VERBOSE: un booléen qui indique si vous souhaitez afficher des informations détaillées sur le transfert des e-mails.

Avertissements

Le script ne fonctionne qu'avec les fournisseurs de messagerie Gmail, Outlook et Yahoo.
Avant d'utiliser le script, vous devez activer l'IMAP et les applications moins sécurisées pour chaque e-mail que vous souhaitez utiliser avec cet outil.
Si vous souhaitez utiliser cet outil avec un autre fournisseur de boîte e-mail, vous devez rechercher le protocole IMAP et SMTP de ce fournisseur de boîte e-mail et remplacer "imap.gmail.com" par le nouveau.

Remarque

Ce script est fourni à titre d'exemple et n'a pas été testé en profondeur. Il est recommandé de l'utiliser avec prudence et de comprendre les implications de sécurité avant de l'utiliser.
