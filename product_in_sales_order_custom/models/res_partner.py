# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    #---------------------------
    #Fields Declaration
    #---------------------------
    
    partnerwise_umo_ids = fields.One2many('partnerwise.umo' , 'partner_id' ,widget="section_and_note_one2many")
    