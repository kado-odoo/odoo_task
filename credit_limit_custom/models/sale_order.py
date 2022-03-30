# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    #---------------------------
    #Method Declaration
    #---------------------------
    
    def action_confirm(self):
        if self.amount_total > self.partner_id.credit_limit:
            raise UserError('Credit Limit Exceeded! You need to increase the credit limit of this customer to proceed')
        return super(SaleOrder, self).action_confirm()
    
    def _create_invoices(self, grouped=False, final=False):
        if self.amount_total > self.partner_id.credit_limit:
            raise UserError("Credit Limit Exceeded!")
        return super(SaleOrder, self)._create_invoices(grouped, final)