# -*- coding: utf-8 -*-

from odoo import models #, fields, api


class openacademy(models.Model):
    #create data in the datatbase which will be name:
    _name = 'openacademy.openacademy'
    _description = 'openacademy.openacademy'

    name = fields.Char(string='Course Title', required=True, index=True,
                       help='Enter your course title on this field')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Html(string='Description')
    bannar = fields.Binary(string='banner')
    price = fields.Float(string='Price', digits=(5,4)) #digit=(total,decimal)

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
