# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    #---------------------------
    #Fields Declaration
    #---------------------------
    second_discount = fields.Float(string='2nd Disc.%')
    
    #---------------------------
    #Method Declaration
    #---------------------------
    @api.depends('second_discount')
    def _compute_amount(self):
        rec = super(SaleOrderLine, self)._compute_amount()
        for second_discount in self:
            if self.second_discount:
                self.price_subtotal = self.price_subtotal - ((self.second_discount*self.price_subtotal)/100)
        return rec

