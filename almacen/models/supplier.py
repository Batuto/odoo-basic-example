# -*- coding: utf-8 -*-
from openerp import models, fields


class Supplier(models.Model):
	_name = 'supplier'

	name = fields.Char(string = "Nombre", required = True)
	#last_name = fields.Char(string='Apellido(s)')
	phone = fields.Char(string = 'Telefono', required = True)
	address = fields.Char(string = 'Direccion', required = True)
	email = fields.Char(string = 'Correo E.', )
	rfc = fields.Char(string = 'R.F.C.', required = True)
	#store_supplier_id = fields.Many2one('store')