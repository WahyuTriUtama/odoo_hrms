# -*- coding: utf-8 -*-

{
    'name': 'Odoo Payroll Accounting',
    'category': 'Generic Modules/Human Resources',
    'summary': """
          Generic Payroll system Integrated with Accounting,Expense Encoding,Payment Encoding,Company Contribution Management
    """,
    'description': """Odoo Payroll Accounting""",
    'version': '16.0.1.1.0',
    'author': 'Odoo SA, Wahyu',
    'company': '',
    'maintainer': '',
    'website': '',
    'depends': ['hr_payroll_community', 'account'],
    'data': ['views/hr_payroll_account_views.xml'],
    'test': ['../account/test/account_minimal_test.xml'],
    'demo': ['data/hr_payroll_account_demo.xml'],
    'images': [
        'static/description/icon.png',
        'static/description/banner.png'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
