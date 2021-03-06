# -*- coding: utf-8 -*-

from odoo import api, models, modules

class ResUsers(models.Model):
    _name = 'res.users'
    _inherit = ['res.users']
    
    #---------------------------
    #Method Declaration
    #---------------------------
    def name_get(self):
        res = []
        for user in self:
            name = user.name +' / '+ user.login
            res.append((user.id, name))
        return res