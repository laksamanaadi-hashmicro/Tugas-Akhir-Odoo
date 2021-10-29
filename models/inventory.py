from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Inventory(models.Model):
    _inherit = 'product.template'