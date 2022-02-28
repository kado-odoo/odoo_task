# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    #---------------------------
    #Fields Declaration
    #---------------------------
    days_to_deliver = fields.Integer()
