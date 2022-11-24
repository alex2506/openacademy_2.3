# -*- coding: utf-8 -*-
{
    'name': "Open Academy Courses",

    'summary': """
         Telegram group
         Odoo Developer learning
        """,

    'description': """
        Скоростной режим обучения Odoo 15
    """,

    'author': "Alex Ag",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'learning',
    'license': 'LGPL-3',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    # 'board' 2.3.19
    'depends': ['base','board'],
    # always loaded
    # ! order: security, views, menus, data, reports
    'data': ['security/groups.xml',
             'security/ir.model.access.csv',
             'views/courses_views.xml',
             'views/sessions_views.xml',
             'views/partners_views.xml',
             'wizard/wizard_sessions_views.xml',
             'views/dashboard_views.xml',
             'views/menus.xml',
             'reports/report_sessions.xml'],

    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}
