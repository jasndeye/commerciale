from odoo import models,fields,api

class Client(models.Model):
     _name = 'commerciale.client'

     nom = fields.Char(string="Nom du Produit")
     prenom= fields.Float(string="Prix du plat")
     telephone= fields.Binary(string="Photo")
     sexe=fields.Selection([('F','Femme'),('M','Masculin')], string="Sexe")
     mail= fields.Text(string="La description du plat")
     adresse=fields.Char(string="Addresse")
     info_bancaire=fields.Char(string="Information Bancaire")