{
    'name': 'NaturShop Proveedores',
    'version': '1.0',
    'summary': 'Gestión de proveedores de productos naturales',
    'author': 'Pablo García',
    'category': 'Purchases',
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/categoria_views.xml',
        'views/certificacion_views.xml',
        'views/proveedor_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

