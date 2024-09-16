from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)

class set_can_be_purchased(models.TransientModel):
    _name = "set.can.be.purchased"
    _description = "set can be purchased"

    def confirm(self):
        pass
        # record_ids = self._context('needed_id', [])
        # _logger(f"-----------------------i am here ---------------------------------------------------------- {record_ids}") 