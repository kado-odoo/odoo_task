# -*- coding: utf-8 -*-

{
    #  Information
    'name':'Product Unique code ',
    'version': '15.0',
    'summary': 'Product Unique code ',
    'description':'Product Unique code ',
    'category':'sales',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        # 'security/security_group.xml',
        # 'security/ir.model.access.csv',
        'views/product_category_views.xml',
        'data/sequence.xml',
    ],
    'depends':['sale_management','purchase'],
    'demo':[],
    
    # Other
    'application':True,
    'installble':True,
}