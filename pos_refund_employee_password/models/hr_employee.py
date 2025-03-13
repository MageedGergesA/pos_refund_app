from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    pos_refund_password = fields.Char(string='POS Refund Password')


    @api.constrains('pos_refund_password')
    def _check_refund_password(self):
        for rec in self:
            if rec.pos_refund_password and not rec.pos_refund_password.isdigit():
                raise models.ValidationError(
                    "Invalid password format. Password can only contain digits."
                )

    @api.model
    def get_pos_pswd(self, employee):
        employee = self.search([('id', '=', employee)], limit=1)
        print(f'empl--------------------------------------------------------{employee}oyee')
        return employee.pos_refund_password if employee else False
