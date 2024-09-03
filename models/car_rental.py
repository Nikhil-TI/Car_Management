from odoo import models, fields

class car_rental(models.Model):
    _name = "car.rental"
    _description = "Car rental records"

    #car id
    car_id = fields.Many2one("car.management" ,string="Car", required=True)

    #borrower id
    borrower_id = fields.Many2one("borrower.details", string="Borrower")

    # rental starting date
    rental_start = fields.Date(String="Starting data")

    #rental ending date
    rental_end = fields.Date(String="Ending data")

    #cost of rental
    cost = fields.Float(String="Cost of rental per month")