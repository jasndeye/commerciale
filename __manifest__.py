# -*- coding: utf-8 -*-
{
    'name': "Commerciale",

    'sequence': 2,

    'description': """
        gestion et le suivi des activités de taf_tech informatique
    """,

    'author': "Melax_dev",
    'website': "https://gitlab.melaximport.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
            #'views/assets.xml',
            # 'views/client.xml',
            # 'views/commandeclient.xml',
            # 'views/commandefournisseur.xml',
            # 'views/factureclient.xml',
            # 'views/facturefournisseur.xml',
            # 'views/menu.xml',
            # 'views/personnel.xml',
            # 'views/produit.xml',
            # 'menu/menu.xml',
            # 'report_facture.xml'
    ],
    # only loaded in demonstration mode
    'installable': True,
    'auto_install': False,
    'application':True,
}