# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductDetailAdditional(models.Model):
    _inherit = "product.template"

    bioequivalente = fields.Boolean(string="Bioequivalente",
                                    help="Indica si es bioequivalente o no")
    principioActivo = fields.Char(string="Principio Activo",
                                  help="Indicar el principio activo")
    dosis = fields.Char(string="Dosis",help="Indicar la dosis del envase")
    laboratorio = fields.Char(string="Laboratorio",help="Indicar laboratorio")
    presentacion = fields.Char(string="Presentación",
                               help="Indicar presentación del medicamento")
