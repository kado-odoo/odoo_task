# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move.line'
    
    second_discount = fields.Float(string='2nd Disc.%')
    
    # @api.onchange('quantity', 'discount', 'price_unit', 'tax_ids', 'second_discount')
    # def _onchange_price_subtotal(self):
    #     record = super(AccountMove, self)._onchange_price_subtotal()
    #     for second_discount in self:
    #         if self.second_discount:
    #             self.price_subtotal = self.price_subtotal - ((self.second_discount*self.price_subtotal)/100)
    #     return record