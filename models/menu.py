# -*- coding: utf-8 -*-

from odoo import models, fields, api

class menu(models.Model):

     _name = 'commerciale.menu'

     nom=fields.Char(string="Nom du menu")
     produit_ids = fields.Many2many('commerciale.produit')
     date_menu = fields.Date(string="Date du menu", default=fields.Date.today)
     # controle de l'unicité sur la date du menu
#      _sql_constraints = [ ('id_unique','UNIQUE(date_menu)', "On doit avoir un menu par jour")]
#       # on force la date a etre la date d'aujord'hui
#      @api.onchange('date_menu')
#      def _Verifier_date_menu(self):
#                if self.date_menu!=fields.Date.today():
#                      raise models.ValidationError("La date du menu doit etre la date d'haujordhui")
