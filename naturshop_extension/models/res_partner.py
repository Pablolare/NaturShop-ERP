from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    tipo_cliente = fields.Selection([
        ('particular', 'Particular'),
        ('empresa', 'Empresa'),
        ('mayorista', 'Mayorista'),
        ('minorista', 'Minorista'),
    ], string='Tipo de cliente', default='particular')
