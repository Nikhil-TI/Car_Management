from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class Car(models.Model):
    
    _inherit = "product.template"

    owner_id = fields.Many2one("res.partner", string="Owners")

    car_type = fields.Selection([("mini","Mini"),("suv","SUV"), ("sports","Sports Car"), ("budget","Budget Friendly"), ("modified", "Modified")], string="Category")

    car_reference = fields.Char(string="Reference", default="new", readonly=True)

    # using context to set the default value of th e field
    purchase_ok = fields.Boolean(readonly=True)

    barcode = fields.Char(compute="copy_barcode", readonly=True)

    location = fields.Char(string="Current Location")


    # add theses
    # override price ranges like cannot be nagative, min - 10,00
    # add sequences like s0001, s002, s003

    @api.depends("car_reference")
    def copy_barcode(self):
        for record in self:
            if record.car_reference:
                record.barcode = record.car_reference
            else:
                record.barcode = "No Barcode"
    
    @api.constrains("list_price")
    def validate_price(self):
        for record in self:
            if record.list_price < 0:
                raise ValidationError("Price cannot be negative!")
            if record.list_price < 1000:
                raise ValidationError("Min price for rental is 1000!")
    
    @api.model_create_multi
    def create(self, vals_list):
        creation_allowed = self.env['ir.config_parameter'].sudo().get_param('car_model.enable_creation')
        if not creation_allowed:
            raise ValidationError("You cannot create a new record!")
        for vals in vals_list:
            if vals.get('car_reference', 'new') == 'new':
                _logger.info(f"*******************%%%%%%%%%%%%%%*********************  {self.env['ir.sequence'].next_by_code('product.template')}  **********%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&")
                vals['car_reference'] = self.env['ir.sequence'].next_by_code('product.template')
        return super().create(vals_list)
    

    def toggle_purchased_value(self):
        self.purchase_ok = not self.purchase_ok
    



    def set_can_be_purchased_dialog_box(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirmation',
            'res_model': 'set.can.be.purchased',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'needed_id': self.id
            }
        }