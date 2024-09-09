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
            
            
            #check is the car is not already rented by another person
            for car in record.car_id:
                overlapping_rentals = self.env["car.rental"].search([
                    ("car_id","in",car.ids),
                    ("id","!=",record.id),
                    ("rental_start","<=", record.rental_end),
                    ("rental_end",">=", record.rental_start)
                ])

                #check if the car is not already rented by the same user
                if overlapping_rentals.borrower_id == record.borrower_id:
                    raise ValidationError(f"You have already rented the car between the date '{overlapping_rentals[0].rental_start}' and '{overlapping_rentals[0].rental_end}'")

                if overlapping_rentals:
                    raise ValidationError(f"The car '{car.model}' is already rented between '{overlapping_rentals[0].rental_start}' and '{overlapping_rentals[0].rental_end}'")


    #calculating the total cost for the rental period
    @api.depends("rental_start", "rental_end")
    def _cal_cost_for_rental(self):
        for record in self:
            if record.rental_start and record.rental_end:
                #calculate the cost for all the selected car for a single day
                totalCost = 0
                for cars in record.car_id:
                    totalCost = totalCost + cars.cost
                
                #fine the total cost for the particular rental slip
                record.total_cost = (record.rental_end - record.rental_start).days * totalCost 
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