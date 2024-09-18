from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)

class set_can_be_purchased(models.TransientModel):
    _name = "set.can.be.purchased"
    _description = "set can be purchased"

    def confirm(self):
        record_id = self._context.get('needed_id', [])
        cars = self.env['product.template'].browse(record_id)
        _logger.info(f"-----------------------i am here ---------------------------------------------------------- {type(cars)}")
        for car in cars:
            car.toggle_purchased_value()