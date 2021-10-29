# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class laksamana_economic_chamber(models.Model):
#     _name = 'laksamana_economic_chamber.laksamana_economic_chamber'
#     _description = 'laksamana_economic_chamber.laksamana_economic_chamber'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
