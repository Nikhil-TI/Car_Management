from odoo import models, fields, api
import uuid

import logging
_logger = logging.getLogger(__name__)

class car_owner(models.Model):
    _inherit = "res.partner"

    barcode = fields.Integer(default= lambda self : uuid.uuid4().int % 10000000000)


    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    @api.model
    def create(self, vals):
        self.ensure_one()
        res=super(car_owner, self).create(vals)
        new_uuid = uuid.uuid4()
        res.barcode= new_uuid.int
        return res


    def set_barcode(self):
        records=self.env['res.partner'].search([('barcode','=','0')])
        _logger.info(f"Display {records}")
        for rec in records:
            rec.barcode=10

        return True