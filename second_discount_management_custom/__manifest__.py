{
    #  Information
    'name':'Second Discount Management',
    'version': '15.0',
    'summary': 'Second Discount Management',
    'description':'Second Discount Management',
    'category':'',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        'views/sale_order_line_views.xml',
        'views/account_move_line_views.xml',
        'report/sale_order_template.xml',
        'report/account_move_template.xml',
        'data/mail_template.xml',
        ],
    'depends':['sale_management'],
    'demo':[],
    # Other
    'application':True,
    'installble':True,
}
