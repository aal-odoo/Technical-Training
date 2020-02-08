# -*- coding: utf-8 -*-

from odoo import models, fields


class ForumSchool(models.Model){
    _name = 'forum.school'
    _description = 'Forum School'

    name = fields.Char(string='School Name', required=True, index=True, help='Enter your Schol name')
    address = fields.Html(string='Address')
    responsible_id = fields.Many2one(comodel_name='res.users', required=True,
                        string='Responsible', ondelete='restrict', copy=False)
    created_on = fields.Date(string='Created On', required=True)
}