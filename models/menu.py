# -*- coding: utf-8 -*-

from odoo import models, fields, api

class menu(models.Model):

     _name = 'commerciale.menu'

     produit_ids = fields.Many2many('commerciale.produit')
     date_menu = fields.Date(string="Date du menu", default=fields.Date.today)