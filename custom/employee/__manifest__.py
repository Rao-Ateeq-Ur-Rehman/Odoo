# -*- coding: utf-8 -*-
{
    'name': 'Employee Data Management System',
    'sequence': 0,
    'author': 'Ateeq Ur Rehman',
    'version': '10.50.0',
    'category': 'Employee',
    'summary': 'Employee Data Managemement System',
    'description': """Employee Data Managemement System""",
    'depends': ['base','mail'],
    'data': [
        'F:\odooPrac\custom\employee\security\ir.model.access.csv',
        'F:/odooPrac/custom/views/menu.xml',
        'F:/odooPrac/custom/views/employee_view.xml',
        'F:/odooPrac/custom/views/wfh_employees_view.xml',
        'F:/odooPrac/custom/views/machine_view.xml',
    ],
    'demo': [],
    'application':True,
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend':[
          'employee/static/src/js/mac.js',
          'employee/static/src/xml/mac.xml',
          'employee/static/src/css/mac.css',
        ],
    },
    'license': 'LGPL-3'
}
