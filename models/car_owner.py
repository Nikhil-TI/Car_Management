from odoo import models, fields

class car_owners(models.Model):
    _name = "car.owner"
    _description = "All the owners who own the cars that are to be rented"
    _rec_name = "email" 

    #name of the owner
    name = fields.Char(string="Name")

    #car's owned
    cars_owned = fields.One2many("car.management","owner_id",string="Car's Owned")

    #contact email
    email = fields.Char(string="Email")