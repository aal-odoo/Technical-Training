# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OpenacademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(name='course title', required=True)
    description = fields.Text()

    session_ids = fields.One2many('openacademy.session', 'course_id',string="sessions")
    level = fields.Selection([('1','Easy'),('2','Medium'), ('3','Hard')], string='Difficulty Level')
    