from odoo import models, fields
import uuid

class borrower(models.Model):
    _inherit="res.partner"

    barcode = fields.Integer(default= lambda self : random.randint(1000000000, 9999999999), unique=True, required=True, readonly=True)

    
