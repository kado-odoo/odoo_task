# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    #---------------------------
    #Fields Declaration
    #---------------------------
    zero_stock_approval = fields.Boolean(string="Zero Stock Approval")
    user_group_Chack = fields.Boolean(string="User Group Chack", compute="_check_user_group")
    
    
    #---------------------------
    #Method Declaration
    #---------------------------
    def action_confirm(self):
        for record in self:
            if not record.zero_stock_approval:
                raise UserError("Chack The Feald Approval.")
            return super(SaleOrder,self).action_confirm()
            
    @api.depends('zero_stock_approval','user_group_Chack')
    def _check_user_group(self):
        self.user_group_Chack = self.env.user.has_group('sales_team.group_sale_manager')
            