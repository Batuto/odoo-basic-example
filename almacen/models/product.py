# -*- coding: utf-8 -*-
from openerp import models, fields


class Product(models.Model):
	_name = 'product'

	kind = fields.Selection([(0,'Comestibles'), (1,'Jardineria'), (2,'Farmacia'), (3,'Ferreteria')],)
	name = fields.Char(string = "Nombre")
	price = fields.Float(string = "Precio")
	perishable = fields.Boolean(string = 'Perecedero')
	description = fields.Text(string = 'Descripcion')