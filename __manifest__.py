# -*- coding: utf-8 -*-
{
    'name': "Rectrict locations",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """ Long description of module's purpose """,

    'author': "gmorillom",
    'maintainer': ['gmorillom'],
    'website': "https://github.com/gmorillom",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/rules_data.xml',
        'views/views.xml',
    ],
}
