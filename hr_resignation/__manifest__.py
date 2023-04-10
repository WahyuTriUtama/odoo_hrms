# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Resignation',
    'version': '16.0.1.0.0',
    'summary': 'Handle the resignation process of the employee',
    'author': 'Wahyu',
    'company': '',
    'website': '',
    'depends': ['hr', 'hr_employee_updation', 'mail'],
    'category': 'Generic Modules/Human Resources',
    'maintainer': '',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/resign_employee.xml',
        'views/hr_employee.xml',
        'views/resignation_view.xml',
        'views/approved_resignation.xml',
        'views/resignation_sequence.xml',
    ],
    'images': [
        'static/description/icon.png',
        'static/description/banner.png'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
