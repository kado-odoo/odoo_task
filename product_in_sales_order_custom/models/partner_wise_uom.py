# -*- coding: utf-8 -*-

from odoo import api, fields, models

class PartnerwiseUmo(models.Model):
    _name = "partnerwise.umo"
    
    #---------------------------
    #Fields Declaration
    #---------------------------
    
    product_id = fields.Many2one('product.product', string='Product')
    partner_id = fields.Many2one('res.partner', 'Partner')
    product_uom_category = fields.Many2one(related='product_id.uom_id.category_id')
    product_uom_id = fields.Many2one('uom.uom', string='UOM',domain="[('category_id','=', product_uom_category)]")
    
    #uom_category_id = fields.Many2one(related='product_id.uom_id.category_id')

    