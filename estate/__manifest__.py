# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Productivity',
    'sequence': -100,
    'summary': 'Create a real estate module',
    'description': "Create a real estate module",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}