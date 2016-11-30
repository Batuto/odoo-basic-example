# -*- coding: utf-8 -*-
from openerp import models, fields

class Purchase_detail(models.Model):
	_name = 'purchase_detail'
	
	purchase_id = fields.Many2one('purchase')
	product_id = fields.Many2one('product')
	quantity = fields.Integer(string='Cantidad')
	unitary_price = fields.Float(string='Precio unitario')
	lot = fields.Char(string='Lote')

class Purchase(models.Model):
	_name = 'purchase'

	datestamp = fields.Datetime(string='Fecha-Hora')
	employee_id = fields.Many2one('employee', string='Empleado')
	supplier_id = fields.Many2one('supplier', string='Proveedor')
	total = fields.Float(string='Precio Total')
	purchase_detail_ids = fields.One2many('purchase_detail', 'purchase_id')
