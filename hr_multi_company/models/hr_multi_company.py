# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrAttendanceMultiCompany(models.Model):
    _inherit = 'hr.attendance'

    company_id = fields.Many2one('res.company', 'Company', copy=False, readonly=True, help="Company",
                                 default=lambda self: self.env.user.company_id)


class HrLeaveMultiCompany(models.Model):
    _inherit = 'hr.leave'

    company_id = fields.Many2one('res.company', 'Company', copy=False, readonly=True, help="Company",
                                 default=lambda self: self.env.user.company_id.id)

    @api.onchange('name')
    def dfgb(self):
        print(self.env.user.company_id)


class HrPayslipMultiCompany(models.Model):
    _inherit = 'hr.payslip.run'

    company_id = fields.Many2one('res.company', 'Company', copy=False, readonly=True, help="Company",
                                 default=lambda self: self.env.user.company_id)


class HrSalaryCategoryMultiCompany(models.Model):
    _inherit = 'hr.salary.rule.category'

    company_id = fields.Many2one('res.company', 'Company', copy=False, readonly=True, help="Comapny",
                                 default=lambda self: self.env.user.company_id)
