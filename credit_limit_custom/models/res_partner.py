# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    #---------------------------
    #Fields Declaration
    #---------------------------
    
    credit_limit = fields.Float(string='Credit Limit')
    total_receivable = fields.Float(string='Total Receivable')