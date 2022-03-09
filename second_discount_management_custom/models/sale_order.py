# -*- coding: utf-8 -*-

from odoo import models, api

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    #---------------------------
    #Method Declaration
    #---------------------------

    def _create_invoices(self, grouped=False, final=False):
        res = super(SaleOrder, self)._create_invoices(grouped, final)
        for record in self:
            record.invoice_ids.invoice_line_ids.second_discount = record.order_line.second_discount
        return res