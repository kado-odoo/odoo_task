# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    
    is_sale_user = fields.Boolean(string='Sale User', config_parameter='res_config_settings_custom.is_sale_user')
    sale_parson = fields.Many2one('res.users', string='Sale Parson', config_parameter='res_config_settings_custom.sale_parson')