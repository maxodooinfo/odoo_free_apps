# -*- coding: utf-8 -*-
{
    'name': 'Attendance Details',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 1,      
    'summary': 'Show attendance details on button hover.',
    'author': 'max',
    'website': '',
    'depends': ['hr_attendance'],
    'data': [
        'views/assets.xml'
    ],
    'qweb': [
        'static/src/xml/attendance.xml',
    ],
    "auto_install": False,
    "installable": True,
    "images":['static/description/banner.png'],
}

