# -*- coding: utf-8 -*-
{
    'name': "citasmdt",

    'summary': """
        Es un modulo propio diseñado para llevar el control de citas.""",

    'description': """
        Es un modulo para llevar el control de citas.
  """,

    'author': "Manuel Fco Domínguez Tienda",
    'website': "https://www.educacionadistancia.juntadeandalucia.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/citasmdt.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
