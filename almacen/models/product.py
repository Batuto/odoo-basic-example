# -*- coding: utf-8 -*-
from openerp import models, fields


class Product(models.Model):
	_name = 'product'

	kind = fields.Selection([(1,'Comestibles'), (2,'Jardineria'),
							(3,'Farmacia'), (4,'Ferreteria')],
							string='Tipo de producto')
	name = fields.Char(string = "Nombre")
	price = fields.Float(string = "Precio")
	perishable = fields.Boolean(string = 'Perecedero')
	description = fields.Text(string = 'Descripcion')
	#store_product_id = fields.One2many()
