# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    #---------------------------
    #Fields Declaration
    #---------------------------
    
    sale_parson = fields.Char(String="Name", default='Kamla')
    is_sale_user = fields.Boolean(string='Sale User', compute="_check_user_from_settings")
    
    #---------------------------
    #Method Declaration
    #---------------------------
    
    @api.depends('name')
    def _check_user_from_settings(self):
        for res in self:
            res.is_sale_user = self.env['ir.config_parameter'].sudo().get_param('res_config_settings_custom.is_sale_user')
        
    @api.model
    def create(self,vals):
        res = super(SaleOrder,self).create(vals)
        conf_user_id= self.env['ir.config_parameter'].sudo().get_param('res_config_settings_custom.sale_parson')
        if conf_user_id:
            res.user_id = conf_user_id
        return res
