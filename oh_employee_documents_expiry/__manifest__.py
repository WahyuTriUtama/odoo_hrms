# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Employee Documents',
    'version': '16.0.1.0.0',
    'summary': """Manages Employee Documents With Expiry Notifications.""",
    'description': """OH Addon: Manages Employee Related Documents with Expiry Notifications.""",
    'live_test_url': 'https://youtu.be/4fe5tzAG8Ng',
    'category': 'Generic Modules/Human Resources',
    'author': 'Wahyu',
    'company': '',
    'maintainer': '',
    'website': "",
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_document_view.xml',
        'views/document_type_view.xml',
        'views/hr_document_template.xml',
    ],
    'demo': ['data/demo_data.xml'],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
