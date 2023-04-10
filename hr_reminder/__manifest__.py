# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Reminders Todo',
    'version': '16.0.1.0.0',
    'category': 'Generic Modules/Human Resources',
    'summary': 'HR Reminder For OHRMS',
    'author': 'Wahyu',
    'company': '',
    'website': "",
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_reminder_security.xml',
        'views/hr_reminder_view.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'hr_reminder/static/src/css/notification.css',
            'hr_reminder/static/src/scss/reminder.scss',
            'hr_reminder/static/src/js/reminder_topbar.js',
            'hr_reminder/static/src/xml/reminder_topbar.xml'
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
