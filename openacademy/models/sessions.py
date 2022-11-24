# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OA_Session(models.Model):
    _name = 'openacademy.session'
    _description = 'openacademy.sesion_description'
    name = fields.Char('Name of session', required=True)
    start_date = fields.Date('Start Date', default=fields.Date.today())
    duration = fields.Integer()
    stop_date = fields.Date(string='End learning', compute="_stop_date",store=True)
    number_of_seats = fields.Integer('Number of seats')
    active = fields.Boolean(string='Active', default=True)
    course_id = fields.Many2one(comodel_name='openacademy.course', string='Course_id',required=True)
    attendees_id = fields.Many2many(comodel_name='res.partner', string = "Attendees_id")
    instructor = fields.Many2one(comodel_name='res.partner', string='Instructor',
                                       domain=['|', ('inh_is_instructor', '=', True),
                                               '|', ('inh_teacher', '=', 'teacher_level1'),
                                                    ('inh_teacher', '=', 'teacher_level2')])
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    number_of_attendees = fields.Integer(string='Number of Attendees', compute="_number_of_attendees", store=True)

    @api.depends('number_of_seats', 'attendees_id')
    def _taken_seats(self):
           for record in self:
               if not record.number_of_seats:
                   record.taken_seats = 0.0
               else:
                   record.taken_seats = 100.0 * len(record.attendees_id) / record.number_of_seats

    @api.depends('attendees_id')
    def _number_of_attendees(self):
        for record in self:
            record.number_of_attendees = len(record.attendees_id)

    @api.depends('start_date', 'duration')
    def _stop_date(self):
        for record in self:
            if record.duration == 0:
                record.stop_date = record.start_date
            else:
                record.stop_date = record.start_date + datetime.timedelta(days=record.duration -1)


    @api.onchange('number_of_seats', 'attendees_id')
    def _verify_valid_number_of_seats(self):
        if self.number_of_seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'number_of_seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.number_of_seats < len(self.attendees_id):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",},}

    @api.constrains('instructor', 'attendees_id')
    def _instructor_in_attendees(self):
        for record in self:
            if record.instructor in record.attendees_id:
                raise ValidationError("A session's instructor can't be an attendee")
