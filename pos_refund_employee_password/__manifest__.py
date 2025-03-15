# -*- coding: utf-8 -*-
{
    'name': 'Restrict POS Refund With Password For Employees',
    'version': '15.0.1.0.0',
    'category': 'Point of Sale',
    'summary': """SecureRefund: Safeguarding POS Transactions""",
    'description': """Enhance security by implementing a password requirement 
     for POS refunds, ensuring controlled access to refund 
     transactions.""",
    'author': 'MGA',
    'company': 'MGA',
    'maintainer': 'MGA',
    "license": "LGPL-3",
    "urrency": "USD",
    "price": "20.0",
    'depends': ['web', 'base', 'point_of_sale', 'hr'],
    'data': [
        'views/views.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'pos_refund_employee_password/static/src/js/refund_password.js'
        ],
    },
    "images": ["static/description/icon.png"],
    'installable': True,
    'application': False,
    'auto_install': False,
}
