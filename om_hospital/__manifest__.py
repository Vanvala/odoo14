# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.agbuda.by',
    'licence': 'LGPL-3',
    'depends': ['sale',
                'mail'
                ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
