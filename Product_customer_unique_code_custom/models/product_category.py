# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductCategory(models.Model):
    _inherit = "product.category"

    #---------------------------
    #Fields Declaration
    #---------------------------
    assign_sequence = fields.Boolean(string="Assign Sequence")