{
    'name': 'NaturShop Extension Clientes',
    'version': '1.0',
    'summary': 'Añade campo tipo de cliente a res.partner',
    'author': 'Pablo García',
    'category': 'Sales',
    'depends': ['base', 'sale'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
