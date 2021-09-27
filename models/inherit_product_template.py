# -*- coding: utf-8 -*-
###############################################################################
#
#    Consultoría en Negocios y ERP, S.A. de C.V.
#    Copyright (C) 2021 Consultoría en Negocios y ERP, S.A. de C.V. 
#    (<https://alfa365.odoo.com>).
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError,AccessError, UserError, RedirectWarning, Warning
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)
import requests
import json
import subprocess

class ProductTemplate(models.Model):
	_inherit = "product.template"

	#rferrer: Metodo para ejecutar exportacion directa de la BD
	def action_view_export_test(self,location_id):
		file_name = 'Archivo'+'.csv'
		final_data = ''
		local_dict = locals()
		exec(open("/home/elfuhrer/develop/dev_free/dev_acs/inherit_stock/models/script1.py").read(),globals(),local_dict)
		# subprocess.call(['/home/elfuhrer/develop/dev_free/dev_acs/inherit_stock/models/script1.py', str(location_id.id)])
		with open('/home/elfuhrer/develop/dev_free/dev_acs/inherit_stock/models/stock_quant.csv') as f:
			contents = f.read()
			print(contents)
			file_data = contents
			final_data = final_data + file_data + '\r\n'
		values = {
			'file_name': file_name,
			'file_data': final_data,
		}
		return values