from odoo import models, fields, api
from odoo.exceptions import UserError

class StockLocation(models.Model):
    _inherit = 'stock.location'

    restrict_location = fields.Boolean(string='Restrict location',default=False)


class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_restricted_locations = fields.Many2many('stock.location',string='Allowed locations')
