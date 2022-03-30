{
    #  Information
    'name':'Sale Order Custom',
    'version': '15.0',
    'summary': 'Sale Order Custom',
    'description':'Sale Order Custom',
    'category':'',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        'wizards/wizard_views.xml',
        'views/sale_wizard_views.xml',
        'security/ir.model.access.csv',
        
        ],
    'depends':['sale_management'],
    'demo':[],
    # Other
    'application':True,
    'installble':True,
}
