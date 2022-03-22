# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        res = []
        for partner in self:
            name = partner.name +' / '+ partner.country_id.name
            res.append((partner.id, name))
        return res
    
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name',operator,name),('phone',operator,name),('email',operator,name)]
        return self._search(domain + args, limit=limit, access_rights_uid = name_get_uid    )
        