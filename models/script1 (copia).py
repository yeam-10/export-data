# -*- coding: utf-8 -*-
###############################################################################
#
#    BroadTech IT Solutions Pvt Ltd
#    Copyright (C) 2018 BroadTech IT Solutions Pvt Ltd 
#    (<http://broadtech-innovations.com>).
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

from os import closerange
import psycopg2
import sys
import pprint
import csv
import pandas as pd

print('*******************EXPORTANDO DATOS******************************')
# conn_string = "host='127.0.0.1' dbname='11-0' user='postgres' password='postgres'"
conn_string = "host='192.168.1.1' dbname='alfasoluciones-redstareco-calidad23-3276887' user='p_alfasoluciones_redstareco_calidad23_3276887' password='admin'"
print ("connecting to the database\n ->%s"%(conn_string))

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

cursor.execute("""
	SELECT 
		p.default_code,
		q.quantity,
		pt.name
	FROM stock_quant q
		JOIN product_product p
		ON q.product_id = p.id
		JOIN product_template pt
		ON p.product_tmpl_id = pt.id
	WHERE location_id = """+str(location_id.id)+"""
""")

records = cursor.fetchall()

# pprint.pprint(records)

data = {}
code_list = []
qty_list = []
product_name_list = []
    
for row in records:
    code_list.append(row[0])
    qty_list.append(row[1])
    product_name_list.append(row[2])
data['Code'] = code_list
data['Cantidad'] = qty_list
data['Producto'] = product_name_list
csvdata = pd.DataFrame(data , columns=['Code','Cantidad','Producto'])
csvdata.to_csv('/home/odoo/src/stock_quant.csv', sep=',',encoding='utf-8', index=False)
print('*******************FIN EJECUCION******************************')