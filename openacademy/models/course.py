# -*- coding: utf-8 -*-

from odoo import models #, fields, api


class openacademy(models.Model):
    #create data in the datatbase which will be name:
    _name = 'openacademy.openacademy'
    _description = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
