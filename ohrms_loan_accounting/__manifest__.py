# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Loan Accounting',
    'version': '16.0.1.0.0',
    'summary': 'Odoo HRMS Loan Accounting',
    'description': """
        Create accounting entries for loan requests.
        """,
    'category': 'Generic Modules/Human Resources',
    'author': "Wahyu",
    'company': '',
    'maintainer': '',
    'website': "",
    'depends': [
        'base', 'hr_payroll_community', 'hr', 'account', 'ohrms_loan',
    ],
    'data': [
        'views/hr_loan_config.xml',
        'views/hr_loan_acc.xml',
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
