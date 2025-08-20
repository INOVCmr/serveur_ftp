# -*- coding: utf-8 -*-
{
    'name': "serveur_ftp",

    'summary': "Ce module permet d'envoyer un fichier dans un serveur FTP à partir des accès du serveur en question.",

    'description': """
                • A partir des accès à serveur FTP pouvoir envoyer un fichier
                • Gérer les fichiers pdf, txt, image, etc
                • Envoyer les fichiers en fonction d'une fréquence d'envoie
    """,

    'author': "INOV CAMEROON",
    'website': "https://www.inov.cm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Gestion des serveurs FTP',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mail'],

    # always loaded
    'data': [

        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/serveur_ftp.xml',
        'security/security.xml',
        #'data/cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    #'images': ["static/description/icon-ftp.png"],
    #'icon': '/serveur-ftp/static/src/img/icon-ftp.png', 
    'application': True,
    'installable': True,
    'auto_install': False, 
    #'license': 'LGPL-3',
}

