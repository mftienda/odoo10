# -*- coding: utf-8 -*-
from odoo import http

# class Citasmdt(http.Controller):
#     @http.route('/citasmdt/citasmdt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasmdt/citasmdt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasmdt.listing', {
#             'root': '/citasmdt/citasmdt',
#             'objects': http.request.env['citasmdt.citasmdt'].search([]),
#         })

#     @http.route('/citasmdt/citasmdt/objects/<model("citasmdt.citasmdt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasmdt.object', {
#             'object': obj
#         })