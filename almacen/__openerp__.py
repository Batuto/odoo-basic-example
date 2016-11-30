# -*- coding: utf-8 -*-
{
    'name': "Almcacen",

    'summary': """Almacen para la materia.""",

    'description': """
        
    """,

    'author': "Mariano Fernandez",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       'views/product_view.xml',
       'views/supplier_view.xml',
       'views/purchase_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
}
