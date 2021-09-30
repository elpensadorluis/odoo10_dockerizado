# -*- coding: utf-8 -*-
{
    'name': "Room Manager",

    'summary': """
        Create and manage rooms
        ver 0.3 in progress
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "bluepoint2",
    'website': "https://www.bluepoint2.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Room',
    'version': '3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/room_menu.xml',
        'views/room_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': 'true',
}
