from odoo import models, fields

class CertificacionEcologica(models.Model):
    _name = 'naturshop.certificacion'
    _description = 'Certificación ecológica'

    name = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='Código')
    descripcion = fields.Text(string='Descripción')
    fecha_caducidad = fields.Date(string='Fecha de caducidad')
    activo = fields.Boolean(string='Activo', default=True)
