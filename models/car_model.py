from odoo import models, fields

class Car(models.Model):
    
    _inherit = "product.product"

    name = fields.Char(string="Car Model")
