# -*- coding: utf-8 -*-
# from odoo import http


# class Serveur-ftp(http.Controller):
#     @http.route('/serveur-ftp/serveur-ftp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/serveur-ftp/serveur-ftp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('serveur-ftp.listing', {
#             'root': '/serveur-ftp/serveur-ftp',
#             'objects': http.request.env['serveur-ftp.serveur-ftp'].search([]),
#         })

#     @http.route('/serveur-ftp/serveur-ftp/objects/<model("serveur-ftp.serveur-ftp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('serveur-ftp.object', {
#             'object': obj
#         })

