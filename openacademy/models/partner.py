from odoo import fields, models, api


class OA_Partner(models.Model):
    _inherit = 'res.partner'

    session_id = fields.Many2many(comodel_name='openacademy.session', readonly=True)
    inh_is_instructor = fields.Boolean('Is_instructor', default=False)
    inh_teacher = fields.Selection([('teacher_level1', "Teacher / Level 1"), ('teacher_level2', "Teacher / Level 2")])
