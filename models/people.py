from odoo import models, fields, api
import random
import logging
_logger = logging.getLogger(__name__)

class people(models.Model):
    _inherit = "res.partner"

    barcode = fields.Integer(default= lambda self : random.randint(100000, 999999), unique=True, required=True, readonly=True)

    isOwner = fields.Boolean(string="Are you a owner?", required=True, default=False)

    car_id = fields.One2many("product.product",string="Cars", inverse_name="owner_id")

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





    #btn to re-generate barcode
    def set_barcode(self):
        # _logger.info(f"{self} -------------------------------------------- LOGIC REACHED HERE -----------------------------------------------------------------")
        self.barcode = random.randint(1000000, 9999999)


    # btn to set the barcode for previous data
    # def set_barcode(self):
    #     records=self.env['res.partner'].search([('barcode','=',0)])
    #     _logger.info(f"Display {len(records)}")
    #     _logger.info(f"----------------------------heloooooooooooooooooooooooooooooooOO-----------------------------------------------")
    #     for rec in records:
    #         barcode = random.randint(1000000, 9999999)
    #         rec.barcode = barcode
