# -*- coding: utf-8 -*-
# from odoo import http


# class Forum(http.Controller):
#     @http.route('/forum/forum/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/forum/forum/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('forum.listing', {
#             'root': '/forum/forum',
#             'objects': http.request.env['forum.forum'].search([]),
#         })

#     @http.route('/forum/forum/objects/<model("forum.forum"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('forum.object', {
#             'object': obj
#         })
