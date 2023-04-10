# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Multi-Company',
    'version': '16.0.1.0.0',
    'summary': """Enables Multi-Company""",
    'description': 'This module enables multi company features',
    'category': 'Generic Modules/Human Resources',
    'author': 'Wahyu',
    'company': '-',
    'website': "",
    'depends': ['base', 'hr', 'hr_contract', 'hr_payroll_community', 'hr_expense', 'hr_attendance', 'hr_employee_transfer'],
    'data': [
        'views/hr_company_view.xml',
        'views/multi_company_view.xml',
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
