# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    
    #---------------------------
    #Method Declaration
    #---------------------------
    
    # @api.onchange('product_id', 'product_uom_id')
    # def _onchange_product_id(self):
    #     self.product_id, self.order_partner_id
    #     if self.product_id and self.order_partner_id:
    #         self.product_uom = self.order_partner_id.partnerwise_umo_ids.filtered(lambda ul : ul.product_id.id == self.product_id.id).product_uom_id.id
    #         print('....................', self.product_uom.name)
    
    @api.onchange('product_id')
    def uom_change(self) :
     for rec in self :
        uom_ids = rec.order_id.partner_id.partnerwise_umo_ids
        for record in uom_ids:
            if rec.product_id == record.product_id:
                rec.product_uom = record.product_uom_id       
    # @api.onchange('product_id', 'product_uom_id')
    # def _onchange_product_id(self):
    #     self.product_id, self.order_partner_id
    #     if self.product_id and self.order_partner_id:
    #         self.product_uom = self.order_partner_id.filtered(lambda ul : ul.product_id.id == self.product_id.id).product_uom_id.id
    #         print('....................', self.product_uom.name)
    