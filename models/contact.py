from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Contact(models.Model):
    _inherit = 'res.partner'

    # so_ids = fields.One2many(
    #     comodel_name='lec.salesorders', 
    #     inverse_name='pembeli_id', 
    #     string='Nama Order Penjualan')
