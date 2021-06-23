from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True, tracking=True)
    ref = fields.Char(string='Reference', required=True, tracking=True, copy=False,
                      readonly=True, default=lambda self: _('New'))
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other', tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string='Status', tracking=True)
    responsible_id = fields.Many2one(comodel_name='res.partner', string="Responsible", tracking=True)
    appointment_count = fields.Integer(string='Appointments', compute='_compute_appointment_count')

    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
    #     select count * from hospital.appointment where patient_id = 5

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
        if values.get('ref', _('New')) == _('New'):
            values['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        return super(HospitalPatient, self).create(values)

    @api.model
    def default_get(self, fields):
        result = super(HospitalPatient, self).default_get(fields)
        print('result------>', result)
        print('field------------->',fields)
        result['age'] = 50
        return result

