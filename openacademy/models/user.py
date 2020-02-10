# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OpenacademyUser(models.Model):
    _name = 'openacademy.user'
    _description = 'Openacademy User'

    name = fields.Char()
    
    instructor = fields.Boolean(default=False)
    
    session_ids = fields.Many2many('openacademy.session', string="Attended")
    