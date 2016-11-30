# -*- coding: utf-8 -*-
from openerp import models, fields


class Customer(models.Model):
	_name = 'customer'

	name = fields.Char(string="Nombre", required=True)
	phone = fields.Char(string='Telefono', required=True)
	address = fields.Char(string='Direccion', required=True)
	email = fields.Char(string='Correo E.', )
	rfc = fields.Char(string='R.F.C.', required=True)
	sale_ids = fields.One2many('sale', 'customer_id')