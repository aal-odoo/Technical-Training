# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OpenAcademyTags(models.Model):
     _name = 'openacademy.tags
    _description = 'openacademy.tags

    name = fields.Char(string='Name')
    

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
    expire_date = fields.Date(string='Expire After', required=True)

    responsible_id = fields.Many2one(comodel_name='res.users', required=True,
                                     string='Responsible',ondelete='restrict', copy=False)
    
    tag_ids = fields.Many2many(comodel_name='openacademy.tags',relation='rel_course_tags',
                               column1="course_id",column2="Tags",string='Tags')
                    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
