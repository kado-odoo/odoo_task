# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleWizard(models.TransientModel):
    _name = 'sale.wizard'
    _description = 'sale Wizard'
    
    
    def confirm_sale(self):
        print('++++++++++button wizard confirm order__++++++++++++++++++')
        #self.env['sale.order'].action_confirm()
        quotations = self._context.get('active_ids')
        quotations_ids = self.env['sale.order'].browse(quotations)
        for quotation in quotations_ids:
            quotation.action_confirm()