# -*- coding: utf-8 -*-

{
    #  Information
    'name':'Delivery Shipping Custom',
    'version': '15.0',
    'summary': 'Sale  and parchase Module are usefull',
    'description':'delivery_shipping_custom',
    'category':'Sales/CRM',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml'
    ],
    'depends':['base', 'sale_management', 'delivery_ups','stock'],
    # Other
    'application':True,
    'installble':True,
}