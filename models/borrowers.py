from odoo import models, fields

class borrowers(models.Model):
    _name = "borrower.details"
    _description = "This contains the data of all the people who have rented a car"

    #name of the borrower
    name = fields.Char(string="Name")

    # rental records
    rental_id = fields.One2many("car.rental", string="rental Data", inverse_name="borrower_id")

    #car's rented
    cars_rented = fields.Many2many(string="Car's Rented", related="rental_id.car_id")

    #profile picture
    avatar = fields.Image(string="Avatar")

    #contact email
    email = fields.Char(string="Email")