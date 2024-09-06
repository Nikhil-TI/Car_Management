from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

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
    total_cost = fields.Float(string="Total Cost", compute="_cal_cost_for_rental", store=True)

    remaining_days = fields.Integer(string="Remaining days for the rental", compute="_cal_remaining_days")

    #making sure that the rental start data is not greater then rental end i.e both are valid dates
    @api.constrains("car_id", "rental_start", "rental_end")
    def _check_availability_of_car(self):
        for record in self:
            if record.rental_start >= record.rental_end:
                raise ValidationError("Start date must be before the end date!")
            if record.car_id:
                car_id = record.car_id
                if car_id.borrower_id != record.borrower_id:
                    raise ValidationError("You cannot rent the chosen car between the provided date. It has already been booked by another person.")

    #calculating the total cost for the rental period
    @api.depends("rental_start", "rental_end")
    def _cal_cost_for_rental(self):
        for record in self:
            if record.rental_start and record.rental_end:
                record.total_cost = (record.rental_end - record.rental_start).days * record.car_id.cost 
            else:
                record.total_cost = 0

    #calculating the remaining days for the rental
    @api.depends("rental_end")
    def _cal_remaining_days(self):
        for record in self:
            if record.rental_end:
                todays_date = date.today()
                _logger.info(f"This is the result see this---------------{(record.rental_end - todays_date).days}")
                record.remaining_days = (record.rental_end - todays_date).days
                pass
            else:
                record.remaining_days = 0