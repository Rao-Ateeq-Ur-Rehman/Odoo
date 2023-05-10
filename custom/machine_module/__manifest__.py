# -*- coding: utf-8 -*-
{
    'name': 'Machine Module',
    'sequence': -1,
    'author': 'Ateeq Ur Rehman',
    'version': '0.0.0.1',
    'category': 'Machine',
    'summary': 'Machine ERP Module',
    'description': """Machine ERP Module""",
    'depends': ['base','mail'],
    'data': [
        'F:\odooPrac\custom\machine_module\security\ir.model.access.csv',
        # 'F:/odooPrac/custom/machine_module/static/src/machine-status_screen/xml/machine_status_screen.xml',
        'F:/odooPrac/custom/machine_module/views/Machine_view.xml',
    ],
    'demo': [],
    'application':True,
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend':[
          # 'employee/static/src/js/mac.js',
          # 'employee/static/src/xml/mac.xml',
          # 'employee/static/src/css/mac.css',
            'machine_module/static/src/machine-status_screen/xml/machine_status_screen.xml',
            'machine_module/static/src/machine-status_screen/js/machine_status_screen.js',
        ],
    },
    'license': 'LGPL-3'
}
