# -*- coding: utf-8 -*-
{
    'name': "Product Detail Additional",

    'summary': """
        Add Principio Activo, Bioequivalente, dosis, presentación, laboratorio field in Product template
        """,

    'author': "Gonzalo Rojas",
    'website': "http://www.gonzalorojas.com",

    'category': 'Personalización para farmacia',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        "views/product_detail_additional_view.xml",
    ],
}
