# -*- coding: utf-8 -*-
from odoo import models, fields, api

class OA_Course(models.Model):
    _name = 'openacademy.course'
    _description = 'openacademy.course_description'
    name = fields.Char("Title", required=True)
    description = fields.Text("Description_of_Course")
    responsible_user = fields.Many2one(comodel_name='res.users', string='Responsible user')
    session_id = fields.One2many(comodel_name='openacademy.session', inverse_name='course_id', string='Session')

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),]

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}

        default['name'] = 'Copy of ' + self.name

        return super().copy(default=default)