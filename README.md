# Nom du module

FTP Manager

# Description 

A partir de ce module, il est possible d'envoyer à un servuer FTP un fichier situé à un repertoire donné par l'utilisateur de façon répétitive en fonction d'une période définie par l'utilisateur. Ainsi, après l'installation du module, l'utilisateur rempli le formulaire en entrant les informations suivantes : le nouveau nom qu'aura le fichier envoyé dans le serveur FTP, l'adresse du serveur FTP, le nom de l'utilisateur du serveur FTP, le mot de passe FTP, le chemin local du fichier (le rpertoire où se trouve le fichier accompagné de son extension), l'adresse mail où sera envoyé le mail de confirmation d'envoi du fichier ou de l'échec d'envoi du fichier, le nombre d'intervalles d'envoi du fichier, le type d'intervalle (minutes, heures, jours) puis cliquer sur le bouton Envoyer.
Le champ "statut d'upload" affiche l'état dans lequel le fichier se trouve (en attente, succès ou échec).
Le champ "tâche planifié liée" affiche le nom de la tâche planifiée (le nom du cron) auquel est ratachée cet enregistrement.

# Fonctionnalités

Fonctionnalité 1 : Envoyer un fichier dans un serveur FTP
Fonctionnalité 2 : Envoyer un mail en cas d'envoi réussi du fichier et en cas d'échec d'envoi du fichier au serveur FTP
Fonctionnalité 3 : Envoyer automatiquement le fichier à une période définie par l'utilisateur en boucle et à chaque fois envoyé un mail à l'adresse mail

# Structure du module
serveur_ftp
    ├── init.py
    ├── manifest.py
    ├── contollers/
    │ └── init.py
    | └── controllers.py
    ├── demo/
    │ └── demo.xml
    ├── data/
    │ └── cron.xml
    ├── models/
    │ └── models.py
    | └── init.py
    | └── serveur_ftp.py
    ├── views/
    │ └── serveur_ftp.xml
    | └── templates.xml
    | └── views.xml
    ├── security/
    │ └── ir.model.access.csv
    | └── security.xml
    └── README.md

# Installation

1. Copier le module dans le répertoire `addons` de votre Odoo.
2. Mettre à jour la liste des applications depuis l’interface Odoo.
3. Installer le module **serveur_ftp**.

# Configuration 

Votre Odoo doit avoir une configuration SMTP correcte pour pouvoir effectuer l'envoi des mails.

Exemple de configuration SMTP:
1. Aller dans "Paramètres" puis cliquer "Activer le mode développeur"
2. Cliquer sur l'onglet "Technique" dans les paramètres puis cliquer sur "Serveurs de messagerie sortants"
3. Cliquer sur nouveau
4. ![Exemple de configuration du smtp](./static/description/screenshot.png)

# Captures d’écran

![Affichage du module après activation sur odoo](./static/description/menu.png)
![vue liste](./static/description/liste.png)
Cliquer sur le bouton "Nouveau" pour commencer à remplir le formulaire
![vue formulaire](./static/description/formulaire.png)
Cliquer sur le bouton "Envoyer" après avoir rempli le formulaire

# Auteur

- Developpé par : INOV CAMEROON
- Contact : https://www.inov.cm


