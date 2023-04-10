# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Branch Transfer',
    'version': '16.0.1.0.0',
    'summary': 'Employee transfer between branches',
    'category': 'Generic Modules/Human Resources',
    'author': 'Wahyu',
    'maintainer': '',
    'company': '',
    'website': '',
    'depends': ['base',
                'hr',
                'hr_contract',
                'hr_employee_updation',
                ],
    'data': [
        'views/employee_transfer.xml',
        'security/ir.model.access.csv',
        'security/branch_security.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
