# -*- coding: utf-8 -*-

from odoo import models, fields, api

class citasmdt(models.Model):
     _name = 'mdt.citasmdt'
     _order = 'orden'
     autor = fields.Char(string="Autor de la cita")
     cita = fields.Text(string="Cita")
     fecha = fields.Date(string="Fecha de visualización")
     orden = fields.Integer(string="Orden de visualización")
