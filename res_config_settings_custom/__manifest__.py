# -*- coding: utf-8 -*-

{
    #  Information
    'name':'Res Config Settings',
    'version': '15.0',
    'summary': 'Res Config Settings',
    'description':'Res Config Settings',
    'category':'',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        'views/res_config_settings_views.xml',
        'views/sale_order_view.xml',
    ],
    'depends':['sale_management'],
    'demo':[],
    
    # Other
    'application':True,
    'installble':True,
}