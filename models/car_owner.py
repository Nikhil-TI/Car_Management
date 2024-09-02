from odoo import models, fields

class car_owners(models.Model):
    _name = "car.owner"
    _description = "All the owners who own the cars that are to be rented"

    #name of the owner
    name = fields.Char(string="Name")

    #car's owned
    cars_id = fields.One2many("car.management","owner_id",string="Car's Owned")


    #profile picture
    avatar = fields.Image(string="Avatar")

    #contact email
    email = fields.Char(string="Email")