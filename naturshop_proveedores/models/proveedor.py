from odoo import models, fields, api

class ProveedorNatural(models.Model):
    _name = 'naturshop.proveedor'
    _description = 'Proveedor de productos naturales'

    name = fields.Char(string='Nombre', required=True)
    partner_id = fields.Many2one(
        'res.partner',
        string='Contacto en Odoo'
    )
    categoria_id = fields.Many2one(
        'naturshop.categoria',
        string='Categoría'
    )
    certificacion_id = fields.Many2one(
        'naturshop.certificacion',
        string='Certificación ecológica'
    )
    anios_experiencia = fields.Integer(
        string='Años de experiencia'
    )
    fecha_alta = fields.Date(
        string='Fecha de alta',
        default=fields.Date.today
    )
    foto_proveedor = fields.Image(
        string='Foto del proveedor'
    )
    valoracion = fields.Integer(
        string='Valoración (1-5)'
    )
    num_productos = fields.Integer(
        string='Número de productos',
        compute='_compute_num_productos',
        store=True
    )

    @api.depends('partner_id')
    def _compute_num_productos(self):
        for record in self:
            if record.partner_id:
                record.num_productos = record.partner_id.supplier_rank
            else:
                record.num_productos = 0
