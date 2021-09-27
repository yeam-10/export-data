{
    'name': "Inventario por ubicacion",
    'version': '1.0',
    'depends': ['base','stock','product'],
    'author': "Alfa Soluciones",
    'category': 'Category',
    'description': """
     Este modulo se encarga de exportar el invetario segun la ubicacion seleccionada.
     - Las siguientes librerias deben estar instaladas:
        * pandas
        * psycopg2
     Se recomienda utilizar pip para instalarlos
        * pip install pandas
        * pip install psycopg2
    """,
    # data files always loaded at installation
    'data': [

        'wizard/wizard_export.xml',
        'views/inherit_stock.xml'
       
    ],
    # data files containing optionally loaded demonstration data
    #'demo': [
    #    'demo/demo_data.xml',
    #],
}