# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Official Announcements',
    'version': '16.0.1.0.0',
    'summary': """Managing Official Announcements""",
    'description': 'This module helps you to manage hr official announcements',
    'category': 'Generic Modules/Human Resources',
    'author': 'Wahyu',
    'company': '',
    'website': "",
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/reward_security.xml',
        'views/hr_announcement_view.xml',
    ],
    'demo': ['data/demo_data.xml'],
    'images': [
        'static/description/icon.png',
        'static/description/banner.png'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
