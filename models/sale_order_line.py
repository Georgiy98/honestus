from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    code = fields.Char(string='Code', related='product_id.code', store=True)
    honestus_code = fields.Char(string='Honestus Code', related='product_id.honestus_code', store=True)
    honestus_price = fields.Float(string='Honestus Price', related='product_id.honestus_price', store=True)
    margin = fields.Float(compute='_compute_margin', string='Margin', store=True)

    @api.depends('price_unit', 'honestus_price', 'product_id.standard_price')
    def _compute_margin(self):
        for record in self:
            base_price = record.product_id.honestus_price or record.price_unit
            if base_price:
                record.margin = (base_price - record.product_id.standard_price) / base_price
            else:
                record.margin = 0
