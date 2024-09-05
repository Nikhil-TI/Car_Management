from odoo import models, fields, api
from odoo.exceptions import ValidationError

class car_rental(models.Model):
    _name = "car.rental"
    _description = "Car rental records"

    #car id
    car_id = fields.Many2many("car.management", "car_management_rental_rel", "rental_id", "car_id", string="Cars")

    car_color = fields.Char(related="car_id.color")

    #borrower id
    # borrower_id = fields.Many2one("borrower.details", string="Borrower")

    borrower_id = fields.Many2one("borrower.details", string="Borrower")

    # rental starting date
    rental_start = fields.Date(string="Starting data")

    #rental ending date
    rental_end = fields.Date(string="Ending data")

    #cost of rental
    cost = fields.Float(string="Cost of rental per month")



    @api.constrains("car_id", "rental_start", "rental_end")
    def _check_availability_of_car(self):
        for record in self:
            if record.rental_start >= record.rental_end:
                raise ValidationError("Start date must be before the end date!")

            # overlapping_rentals = self.search([("car_id")])
            
        