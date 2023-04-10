# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Employees From User',
    'version': '16.0.1.0.0',
    'summary': 'Automatically Creates Employee While Creating User',
    'description': 'This module helps you to create employees automatically while creating users',
    'category': 'Generic Modules/Human Resources',
    'author': 'Wahyu',
    'company': '',
    'website': "",
    'depends': ['base', 'hr'],
    'data': ['views/employee_creation_from_user_view.xml'],
    'images': [
        'static/description/icon.png',
        'static/description/banner.png'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
