{
    #  Information
    'name':'Product In Sales Order Custom',
    'version': '15.0',
    'summary': 'Product In Sales Order Custom',
    'description':'Product In Sales Order Custom',
    'category':'',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        'views/res_partner_view.xml',
        'security/ir.model.access.csv'
        ],
    'depends':['sale_management','stock','purchase'],
    'demo':[],
    # Other
    'application':True,
    'installble':True,
}
