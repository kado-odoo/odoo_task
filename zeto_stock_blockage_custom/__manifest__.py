# -*- coding: utf-8 -*-

{
    #  Information
    'name':'Zero Stock Blockage',
    'version': '15.0',
    'summary': 'Zero Stock Blockage',
    'description':'Zero Stock Blockage',
    'category':'',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        # 'security/security_group.xml',
        # 'security/ir.model.access.csv',
        'views/sale_order_view.xml'
    ],
    'depends':['sale_management','stock'],
    'demo':[],
    
    # Other
    'application':True,
    'installble':True,
}