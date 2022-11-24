from odoo import models, fields, api

class OA_Sessions_Wizard(models.TransientModel):
    _name = 'openacademy.wizard.sessions'
    _description = 'Open Academy Wizard Sessions&Attendeess'

    def default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_id'))
    sessions_tr_id = fields.Many2many(comodel_name='openacademy.session',
                                  string="Sessions", default=default_session)
    attendees_tr_id = fields.Many2many(comodel_name='res.partner')

    def add_attendees_to_sessions(self):
        for session in self.sessions_tr_id:
            session.attendees_id |= self.attendees_tr_id
        return {}

