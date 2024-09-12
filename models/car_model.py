from odoo import models, fields

class Car(models.Model):
    
    _inherit = "product.product"

    name = fields.Char(string="Car Model")

    people_id = fields.Many2one("res.partner", string="People's")

    # categ_id = fields.Selection([("all","All"),("suv","SUV"), ("sports","Sports Car"), ("budget","Budget Friendly")], string="Category", default="all")


    # add theses
    # override price ranges like cannot be nagative, min - 10,00
    # add sequences like s0001, s002, s003
    