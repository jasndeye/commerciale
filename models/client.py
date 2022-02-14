from odoo import models,fields,api

class Client(models.Model):
     _name = 'commerciale.client'

     nom = fields.Char(string="Nom du Produit")
     prenom= fields.Float(string="Prix du plat")
     telephone= fields.Binary(string="Photo")
     mail= fields.Text(string="La description du plat")
     adresse=fields.Char(string="Addresse")
     info_bancaire=fields.Char(string="Information Bancaire")
     point_fidelite = fields.Integer(string="Point fidélité")