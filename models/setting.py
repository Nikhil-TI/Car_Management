from odoo import models, fields, api

class Setting(models.TransientModel):
    _inherit = "res.config.settings"

    enable_barcode = fields.Boolean(string="Enable barcode generation")
    # enable_creation = fields.Boolean(string="Enable creations")

    def get_values(self):
        res = super(Setting, self).get_values()
        res.update(
            enable_barcode=self.env['ir.config_parameter'].sudo().get_param('people.enable_barcode', default=False)
        )
        return res

    def set_values(self):
        super(Setting, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param('people.enable_barcode', self.enable_barcode)