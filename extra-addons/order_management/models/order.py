from odoo import models, fields, api

class Order(models.Model):
    _name = 'order_management.order'
    _description = 'Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    customer_id = fields.Many2one('res.partner', string='Customer')
    order_lines = fields.One2many('order_management.order_line', 'order_id', string='Order Lines')
    # currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    # total_amount = fields.Monetary(string='Total Amount', compute='_compute_total_amount')

    # @api.depends('order_lines')
    # def _compute_total_amount(self):
    #     # self.total_amount = 0
    #     for order in self:
    #         order.total_amount = sum(order_line.price_subtotal for order_line in order.order_lines)

class OrderLine(models.Model):
    _name = 'order_management.order_line'
    _description = 'Order Line'

    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Integer(string='Quantity', default=1)
    price_unit = fields.Float(string='Unit Price')
    # price_subtotal = fields.Monetary(string='Subtotal', compute='_compute_subtotal')
    order_id = fields.Many2one('order_management.order', string='Order')

    # @api.depends('quantity', 'price_unit')
    # def _compute_subtotal(self):
    #     for line in self:
    #         line.price_subtotal = line.quantity * line.price_unit
