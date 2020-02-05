# -*- coding: utf-8 -*-

from odoo import models, fields

    
class OpenAcademySession(models.Model):
    _name = 'openacademy.session'
    _description =  'OpenAcademy Sessions'
    _order = 'id, start_date'
    
    name = fields.Char(string='Name', required=True, 
                        index=True, help='Enter your course title on this field.')
    active = fields.Boolean(string='Active', default=True)
    course_id = fields.Many2one(comodel_name='openacademy.course', required=True)
    insructor_id = fields.Many2one(comodel_name='res.partner', required=True,
                        string='Instructor', ondelete='restrict', copy=False)
    location_id = fields.Many2one(comodel_name='res.partner', ondelete='restrict')
    code = fields.Char(string='Code', size=32)
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    avail_seat_per = fields.Float(string='Avaliable Seats (%)')
    max_seats = fields.Integer(string='Maximum Seats')
    min_seats = fields.Integer(string='Minimum Required Seats')
    syllabus_notes = fields.Html(string='Syllabus')
    state = fields.Selection(selection=[
                            ('draft', 'New'),
                            ('approve', 'Approved'),
                            ('confirm', 'Confirmed'),
                            ('cancel', 'Cancelled'),
                            ('done', 'Done'),
                        ])