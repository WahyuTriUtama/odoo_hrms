# -*- coding: utf-8 -*-

{
    'name': 'Odoo Employee Contracts Types',
    'version': '16.0.1.1.0',
    'category': 'Generic Modules/Human Resources',
    'summary': """
        Contract type in contracts
    """,
    'description': """Odoo Employee Contracts Types""",
    'author': 'Odoo SA, Wahyu',
    'company': '-',
    'maintainer': '-',
    'website': '',
    'depends': ['hr', 'hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/contract_view.xml',
        'data/hr_contract_type_data.xml',
    ],
    'installable': True,
    'images': ['static/description/icon.png'],
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
