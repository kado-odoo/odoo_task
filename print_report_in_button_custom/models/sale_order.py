# -*- coding: utf-8 -*-

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    #---------------------------
    #Method Declaration
    #---------------------------
    
    def print_report_saleorder(self):
        return self.env.ref('sale.action_report_saleorder').report_action(self)    