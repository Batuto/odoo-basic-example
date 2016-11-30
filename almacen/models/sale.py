# -*- coding: utf-8 -*-
from openerp import models, fields

class Sale_detail(models.Model):
	_name = 'sale_detail'
	
	sale_id = fields.Many2one('sale', string='Venta #')
	product_id = fields.Many2one('product', string='Id Producto')
	quantity = fields.Integer(string='Cantidad')
	discount = fields.Integer(string='Descuento')
	

class Sale(models.Model):
	_name = 'sale'

	datestamp = fields.Datetime(string='Fecha-Hora')
	employee_id = fields.Many2one('employee', string='Empleado')
	total = fields.Float(string='Precio Total')
	customer_id = fields.Many2one('customer', string='Cliente')
	sale_detail_ids = fields.One2many('sale_detail', 'sale_id')
