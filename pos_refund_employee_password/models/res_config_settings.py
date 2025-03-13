# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    """This class used to inherit from res.config.settings(settings) to add the
    field global_refund_security."""
    _inherit = 'res.config.settings'

    global_refund_security = fields.Boolean(help="This field used to allow refund to all employees",
        string='Global Refund', config_parameter='pos_refund_employee_password.global_refund_security')
