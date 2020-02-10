# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OpenacademySession(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.context_today)
    duration = fields.Float(digits=(6,2), help='duration in days', default=1)
    active = fields.Boolean(default=True)
    seats = fields.Integer()
    level = fields.Selection(related='course_id.level', readonly=True)

    
    taken_seats = fields.Float(compute='_compute_taken_seats', store=True) #constaint fields
    

    
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string='Course', required=True)
    instructor_id = fields.Many2one('openacademy.user', string='Instructor')
    student_ids = fields.Many2many('openacademy.user', string='Students')
    
    # method means to seat up a variable
    # stores the percentage of taken seats into 'taken_seats'
    @api.depends('seats','student_ids')
    def _compute_taken_seats(self):
        for session in self:
            if not session.seats:
                session.taken_seats = 0.0
            else:
                session.taken_seats = 100.0 * len(session.student_ids) / session.seats
                
    ## using onchange
    # onchange means to modify an element based on the argument
    # for example: return a warning if 'taken_seat' > 100
    
    @api.onchange('seats', 'student_ids')
    def _compute_taken_seats(self):
        if(self.taken_seats > 100):
            return{'warning': {
                'title': 'Class Full',
                'message': 'The session is full and there is no more space.'
            }}
        
    ##creating constrains
        
    @api.constrains('seats', 'student_ids')
    def _check_taken_seats(self):
        for session in self:
            if session.taken_seats > 100:
                raise exceptions.ValidationError('The session is full at the moment')

    
    ###
    ## using SQL constrains
    ###
    _sql_constraints = [
        # possible only if taken_seats is stored
        ('session_full', 'CHECK(taken_seats <= 100)', 'The room is full'),
    ]