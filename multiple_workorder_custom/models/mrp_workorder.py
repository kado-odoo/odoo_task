# -*- coding: utf-8 -*-

from odoo import api, fields, models

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'
    
    
    #---------------------------
    #Method Declaration
    #---------------------------
    def button_start_mycase(self):
        for order in self:
            if not order.is_user_working:
                order.button_start()
                
    def button_pending_mycase(self):
        for order in self:
            if order.is_user_working :
                    order.button_pending()
                   
    def button_done_mycase(self):
        for order in self:
            if order.is_user_working:
                order.button_finish()