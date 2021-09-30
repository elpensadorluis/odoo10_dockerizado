# -*- coding: utf-8 -*-
from odoo import http

# class CustomModule(http.Controller):
#     @http.route('/room_manager_/room_manager_/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/room_manager_/room_manager_/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('room_manager_.listing', {
#             'root': '/room_manager_/room_manager_',
#             'objects': http.request.env['room_manager_.room_manager_'].search([]),
#         })

#     @http.route('/room_manager_/room_manager_/objects/<model("room_manager_.room_manager_"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('room_manager_.object', {
#             'object': obj
#         })