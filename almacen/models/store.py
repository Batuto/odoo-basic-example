# -*- coding: utf-8 -*-
from openerp import models, fields


class Store(models.Model):
	_name = 'store'

	product_id = fields.Many2one('product')
	lot = fields.Char(string='Lote')
	quantity = fields.Integer(string='Cantidad')
	expiration_date = fields.Date(string='Fecha de caducidad')
	#supplier_id = fields.One2many('supplier', 'rfc')
	supplier_id = fields.Many2one('supplier')
	