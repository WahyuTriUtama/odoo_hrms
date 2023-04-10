# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Advance Salary',
    'version': '16.0.1.0.0',
    'summary': 'Advance Salary In HR',
    'description': """
        Helps you to manage Advance Salary Request of your company's staff.
        """,
    'category': 'Generic Modules/Human Resources',
    'author': "Wahyu",
    'company': '',
    'maintainer': '',
    'website': "",
    'depends': [
        'hr_payroll_community', 'hr', 'account', 'hr_contract', 'ohrms_loan',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/salary_structure.xml',
        'views/salary_advance.xml',
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
