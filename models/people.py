from odoo import models, fields
from odoo.exceptions import ValidationError

import random
import logging
_logger = logging.getLogger(__name__)

class people(models.Model):
    _inherit = "res.partner"

    barcode = fields.Integer(default= lambda self : random.randint(100000, 999999), unique=True, required=True, readonly=True)

    isOwner = fields.Boolean(string="Are you a owner?", required=True, default=False)

    car_id = fields.One2many("product.template",string="Cars", inverse_name="owner_id")

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # @api.model
    # def create(self, vals):
    #     self.ensure_one()
    #     barcode = random.randint(1000000000, 9999999999)
    #     vals["barcode"]= barcode
    #     return super(car_owner, self).create(vals)
    # @api.model
    # def create(self, vals):
    #     self.ensure_one()
    #     res=super(car_owner, self).create(vals)
    #     new_uuid = uuid.uuid4()
    #     res.barcode= new_uuid.int
    #     return res



    def create_values(self):
        message = "Good morning"
        self = self.with_context(random_value = message)
        
        _logger.info(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%---------------------{self._context.get("random_value")}-------------------------------%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    
    def change_value(self):
        message = "Bye-Bye"
        self=self.with_context(random_value = message)
        _logger.info(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%---------------------{self._context.get("random_value")}-------------------------------%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    
    
        

    #btn to re-generate barcode
    def set_barcode(self):
        can_change_barcode = self.env['ir.config_parameter'].sudo().get_param('people.enable_barcode')

        if not can_change_barcode:
            raise ValidationError("You do not have the required permission for changing the barcode!")
        self = self.with_context(using_button = True)
        self.barcode = random.randint(1000000, 9999999)
        self.check_barcode_origin()
    
    def check_barcode_origin(self):
        if self.env.context.get("using_button"):
            _logger.info(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!_______________________---------------------------Logic triggered using button-----------------------___________________________!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            _logger.info(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!_______________________---------------------------Logic triggered without button-----------------------___________________________!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            

            
    # @api.model
    # def search(self, args):
    #     _logger.info(f"-------------------------------------------- LOGIC REACHED HERE -----------------------------------------------------------------")


    # btn to set the barcode for previous data
    # def set_barcode(self):
    #     records=self.env['res.partner'].search([('barcode','=',0)])
    #     _logger.info(f"Display {len(records)}")
    #     _logger.info(f"----------------------------heloooooooooooooooooooooooooooooooOO-----------------------------------------------")
    #     for rec in records:
    #         barcode = random.randint(1000000, 9999999)
    #         rec.barcode = barcode
