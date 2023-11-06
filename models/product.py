from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    honestus_code = fields.Char(string='Honestus Code')
    honestus_price = fields.Float(string='Honestus Price')

    @api.constrains('default_code', 'honestus_code')
    def _check_honestus_code(self):
        for product in self:
            if product.default_code and not product.honestus_code:
                raise ValidationError("Honestus Code is required when Default Code is filled in.")
