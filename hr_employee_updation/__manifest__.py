# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Employee Info',
    'version': '16.0.1.0.0',
    'summary': """Adding Advanced Fields In Employee Master""",
    'description': 'This module helps you to add more information in employee records.',
    'category': 'Generic Modules/Human Resources',
    'author': 'Wahyu',
    'company': '',
    'website': "",
    'depends': ['base', 'hr', 'mail', 'hr_gamification', 'hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/hr_notification.xml',
        'views/contract_days_view.xml',
        'views/updation_config.xml',
        'views/hr_employee_view.xml',
    ],
    'images': [
        'static/description/icon.png',
        'static/description/banner.png'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
