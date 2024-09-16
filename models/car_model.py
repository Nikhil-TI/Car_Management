from odoo import models, fields, api
from odoo.exceptions import ValidationError
class Car(models.Model):
    
    _inherit = "product.product"

    owner_id = fields.Many2one("res.partner", string="Owners")

    car_type = fields.Selection([("mini","Mini"),("suv","SUV"), ("sports","Sports Car"), ("budget","Budget Friendly"), ("modified", "Modified")], string="Category")

    car_reference = fields.Char(string="Reference", default="new", readonly=True)


    # add theses
    # override price ranges like cannot be nagative, min - 10,00
    # add sequences like s0001, s002, s003
    
    @api.constrains("lst_price")
    def validate_price(self):
        for record in self:
            if record.lst_price < 0:
                raise ValidationError("Price cannot be negative!")
            if record.lst_price < 1000:
                raise ValidationError("Min price for rental is 1000!")
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('number', 'new') == 'new':
                vals['car_reference'] = self.env['ir.sequence'].next_by_code('product.product')
        return super().create(vals_list)