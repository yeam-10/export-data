# -*- coding: utf-8 -*-
import base64
from odoo import models, fields, api
from odoo.exceptions import UserError


class WizardExportData(models.TransientModel):
    _name = "wizard.export.data"

    csv_filename = fields.Char()
    csv_binary = fields.Binary()
    location_id = fields.Many2one('stock.location',string="Ubicación",domain=[('usage','=','internal')])
    state = fields.Selection([('choose', 'choose'), ('get', 'get')], default='choose')
 
    @api.multi
    def generate_file(self):
        this = self[0]
        stock = self.env['product.template'].action_view_export_test(self.location_id)
        if stock['file_name']:
            content = stock['file_data']
            file_name = stock['file_name']
            content = content.encode('ascii', 'replace')
            this.write({'state': 'get', 'csv_binary': base64.encodestring(content), 'csv_filename': file_name})


        return {
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.export.data',
            'view_mode': 'form',
            'res_id': this.id,
            'views': [(False, 'form')],
            'target': 'new',
        }