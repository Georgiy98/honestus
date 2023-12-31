{
    'name': 'Honestus',
    'summary': 'Test module for honestus company',
    'category': 'Website/Website',
    'sequence': 20,
    'version': '1.0',
    'depends': [
        'auth_signup',
        'portal',
        'sale',
    ],
    'installable': True,
    'data': [
        'views/mobile_extension.xml',
        'views/product_with_honestus_code_and_price.xml',
        'views/report.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
