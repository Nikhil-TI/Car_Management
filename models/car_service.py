from odoo import fields, models
from odoo.exceptions import ValidationError
from datetime import date

class Car_service(models.Model):
    _name = "car.service"
    _inherit = "car.management"
    _description = "Car service"

    service_type = fields.Selection([
        ("maintenance","Maintenance"),
        ("mot","MOT")
    ], string="Service type", required=True)

    service_date = fields.Date(string="Service Date", required=True)
    next_due_date = fields.Date(string="Next Due Date")

    
    car_id = fields.Many2one("car.management",string="Car", required=True)

    @api.constrains('service_date', 'next_due_date')
    def _check_dates(self):
        for record in self:
            if record.service_date > date.today():
                raise ValidationError("Service date cannot be in the future!")
            if record.next_due_date and record.next_due_date <= record.service_date:
                raise ValidationError("Next due date must be after the service date!")
    