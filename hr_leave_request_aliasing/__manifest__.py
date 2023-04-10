# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Leave Request Aliasing',
    'version': '16.0.1.0.0',
    'summary': """Allows You To Create Leave Request Automatically From Incoming Mails""",
    'description': 'This module allows you to create leave request directly from incoming mails.',
    'category': 'Generic Modules/Human Resources',
    'author': 'Wahyu',
    'company': '',
    'website': "",
    'depends': ['base_setup', 'hr', 'hr_holidays'],

    'data': [
        'views/leave_request_alias_view.xml',
        'views/res_config_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hr_leave_request_aliasing/static/src/js/web_planner_hr_leave.js',
        ],
    },
    'images': [
        'static/description/icon.png',
        'static/description/banner.png'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
