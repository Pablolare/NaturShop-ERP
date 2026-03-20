from odoo import models, fields

class CategoriaNatural(models.Model):
    _name = 'naturshop.categoria'
    _description = 'Categoría de producto natural'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    activo = fields.Boolean(string='Activo', default=True)
