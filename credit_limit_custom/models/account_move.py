# -*- coding: utf-8 -*-

from odoo import models, api , _
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = "account.move"
    
    #---------------------------
    #Method Declaration
    #---------------------------
    
    def action_post(self):
        if self.amount_total > self.partner_id.credit_limit:
            raise ValidationError(_('Credit Limit Exceeded! You need to increase the credit limit of this customer to proceed'))
        return super(AccountMove, self).action_post()