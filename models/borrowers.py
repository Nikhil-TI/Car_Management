from odoo import models, fields

class borrowers(models.Model):
    _name = "borrower.details"
    _description = "This contains the data of all the people who have rented a car"

    #name of the borrower
    name = fields.Char(string="Name")

    #car's rented
    cars_rented = fields.One2many("car.management", "borrower_id",string="Car's rented")

    #contact email
    email = fields.Char(string="Email")