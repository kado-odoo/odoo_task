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
        result=super(SaleOrder,self).action_confirm()
        for record in self:
            if record.zero_stock_approval:
                raise UserError("Ckack The Feald Approval.")
        return result
    
    @api.depends('zero_stock_approval','new_zero_stock')
    def _check_user_group(self):
        if self.env.user.has_group('sales_team.group_sale_manager'):
            self.new_zero_stock = True
        else:
            self.new_zero_stock = False
    
    
    # def _check_user_group(self):
    #     new_zero_stock = False
    #     if self.user.has_group('base.group_sale_manager'):
    #         new_zero_stock = True
   
    #  = self.user.has_group('base.group_sale_manager')
    
    # def action_confirm(self):
    #     for record in self:def _check_user_group(self):
    #     print("Chack The Method........")
    #     #self.group_sale_manager
    #         if record in self.zero_stock_blockage == True:
    #             return super(SaleOrder,self).action_confirm()
           
               
