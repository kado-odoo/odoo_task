# -*- coding: utf-8 -*-

import datetime
from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    #---------------------------
    #Fields Declaration
    #---------------------------
    
    appointment_date = fields.Datetime(string='Appointment Date', readonly=False , store=True)
    #scheduled_date = fields.Datetime(string='Scheduled Date', compute='_compute_scheduled_date' , store=True)
    
    #---------------------------
    #Method Declaration
    #---------------------------
    
    @api.onchange('appointment_date')
    def _onchange_scheduled_date(self):
        for record in self:
            if record.appointment_date and record.partner_id.days_to_deliver > 0:
                record.scheduled_date = record.appointment_date - datetime.timedelta(days=record.partner_id.days_to_deliver)
    
    
    # @api.depends('appointment_date','partner_id')
    # def _compute_scheduled_date(self):
    #     for record in self:
    #         if record.appointment_date and record.partner_id.days_to_deliver :
    #             record.scheduled_date = record.appointment_date - datetime.timedelta(days=record.partner_id.days_to_deliver)
    #         elif not record.appointment_date:
    #             record.sale.order.appointment_date = record.sale.order.appointment_date
    #         else:
    #             record.sale.order.appointment_date = record.sale.order.appointment_date
    
