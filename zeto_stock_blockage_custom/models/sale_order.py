# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    #---------------------------
    #Fields Declaration
    #---------------------------
    zero_stock_approval = fields.Boolean(string="Zero Stock Approval")
    new_zero_stock = fields.Boolean(string="new_zero_stock", compute="_check_user_group")
    
    
    #---------------------------
    #Method Declaration
    #---------------------------
    def action_confirm(self):
        
        for record in self:
            if record.zero_stock_approval:
                super(SaleOrder,self).action_confirm()
            else:
                raise UserError("Ckack The Feald Approval.")
                
       
    
    @api.depends('zero_stock_approval','new_zero_stock')
    def _check_user_group(self):
        self.new_zero_stock = self.env.user.has_group('sales_team.group_sale_manager')
            