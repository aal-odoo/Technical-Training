# -*- coding: utf-8 -*-

from odoo import models,fields

class ForumSchool(models.Model):
    _name = 'forum.school'
    _description = 'Forum School'
    _order = 'id, created_on desc'
    
    name = fields.Char(string="School Name", required=True, index=True, help='Enter your school name')
    address = fields.Html(string="Address")
    responsible_id = fields.Many2one(comodel_name='res.users', required=True, string='Responsible', ondelete='restrict', copy=False)
    created_on = fields.Date(string='Created On', required=True)
