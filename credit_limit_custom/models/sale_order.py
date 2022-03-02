# -*- coding: utf-8 -*-

from unittest import result
from odoo import models, api , _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    #---------------------------
    #Method Declaration
    #---------------------------
    
    def action_confirm(self):
        if self.amount_total > self.partner_id.credit_limit:
            raise ValidationError(_('Credit Limit Exceeded! You need to increase the credit limit of this customer to proceed'))
        return super(SaleOrder, self).action_confirm()
    
    def _prepare_invoice(self):
        if self.amount_total > self.partner_id.credit_limit:
            raise ValidationError(_('Credit Limit Exceeded! You need to increase the credit limit of this customer to proceed'))
        return super(SaleOrder, self)._prepare_invoice()