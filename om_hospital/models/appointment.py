from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"

    name = fields.Char(string='Name', required=True, copy=False, readonly=True,
                       tracking=True, default=lambda self: _('New'))
    patient_id = fields.Many2one(comodel_name='hospital.patient', string="Patient", tracking=True,
                                 required=True)
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', readonly=True)

    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancel')],
                             default='draft', string='Status', tracking=True)
    note = fields.Text(string='Description')
    date_appointment = fields.Date(string='Date', default=lambda self: fields.Datetime.today())
    date_checkup = fields.Datetime(string='Check Up Time', default=lambda self: fields.Datetime.now())

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    def action_draft(self):
        self.state = 'draft'

    @api.model
    def create(self, values):
        if not values.get('note'):
            values['note'] = 'New patient'
        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        return super(HospitalAppointment, self).create(values)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.note:
                self.note = self.patient_id.note
        else:
            self.gender = ''
            self.note = ''