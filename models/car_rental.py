from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class car_rental(models.Model):
    _name = "car.rental"
    _description = "Car rental records"

    #car id
    car_id = fields.Many2many("car.management", "car_management_rental_rel", "rental_id", "car_id", string="Cars", required=True)

    #borrower id
    borrower_id = fields.Many2one("borrower.details", string="Borrower", required=True)

    # rental starting date
    rental_start = fields.Date(string="Starting data", required=True)

    #rental ending date
    rental_end = fields.Date(string="Ending data", required=True)

    #cost of rental
    total_cost = fields.Float(string="Cost of rental per month", compute="_cal_cost_for_rental", store=True)

    @api.constrains("car_id", "rental_start", "rental_end")
    def _check_availability_of_car(self):
        for record in self:
            if record.rental_start >= record.rental_end:
                raise ValidationError("Start date must be before the end date!")

    @api.depends("rental_start", "rental_end")
    def _cal_cost_for_rental(self):
        for record in self:
            if record.rental_start and record.rental_end:
                record.total_cost = (record.rental_end - record.rental_start).days * record.car_id.cost 
                _logger.info(f"This is the result see this---------------{(record.rental_end - record.rental_start).days * record.car_id.cost}")
            else:
                record.total_cost = 0