# -*- coding: utf-8 -*-
# from odoo import http


# class LaksamanaEconomicChamber(http.Controller):
#     @http.route('/laksamana_economic_chamber/laksamana_economic_chamber/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/laksamana_economic_chamber/laksamana_economic_chamber/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('laksamana_economic_chamber.listing', {
#             'root': '/laksamana_economic_chamber/laksamana_economic_chamber',
#             'objects': http.request.env['laksamana_economic_chamber.laksamana_economic_chamber'].search([]),
#         })

#     @http.route('/laksamana_economic_chamber/laksamana_economic_chamber/objects/<model("laksamana_economic_chamber.laksamana_economic_chamber"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('laksamana_economic_chamber.object', {
#             'object': obj
#         })
