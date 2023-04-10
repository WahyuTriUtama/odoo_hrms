# -*- coding: utf-8 -*-

{
    'name': 'Odoo HRMS Core',
    'version': '16.0.1.0.0',
    'summary': """Odoo HRMS Suit: It brings all Odoo HRMS modules""",
    'description': """Odoo HRMS""",
    'category': 'Generic Modules/Human Resources',
    'author': 'Wahyu',
    'company': '',
    'website': "",
    'depends': [
                'base', 'web', 'mail',
                'hr',
                'hr_payroll_account_community',
                'hr_gamification',
                'hr_employee_updation',
                'hr_recruitment',
                'hr_attendance',
                'hr_holidays',
                'hr_payroll_community',
                'hr_expense',
                'hr_leave_request_aliasing',
                'hr_timesheet',
                'oh_employee_creation_from_user',
                'oh_employee_documents_expiry',
                'hr_multi_company',
                'ohrms_loan_accounting',
                'ohrms_salary_advance',
                'hr_reward_warning',
                'hrms_dashboard',
                'hr_reminder',
                'hr_contract_types'
    ],
    'data': [
        'views/menu_arrangement_view.xml',
        'views/hr_config_view.xml',
        'views/menu_item_form_inherit_view.xml',
    ],
    'assets': {
        'web.assets_backend': [

            'ohrms_core/static/src/css/menu_order_alphabets.css',
            'ohrms_core/static/src/js/appMenu.js',
            'ohrms_core/static/src/js/data.js',
            'ohrms_core/static/src/xml/link_view.xml',
            'ohrms_core/static/templates/side_bar.xml'
        ],
    },
    'images': [
        'static/description/icon.png',
        'static/description/banner.png'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
