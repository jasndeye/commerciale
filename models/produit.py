from odoo import models,fields,api

class Produit(models.Model):
     _name = 'commerciale.produit'

     nom = fields.Char(string="Nom du plat")
     prix= fields.Float(string="Prix du plat")
     photo= fields.Binary(string="Photo")
     description= fields.Text(string="La description du plat")
     quantite_stock=fields.Integer(string="Quantité")
     type=fields.Selection([('s','stockable'),('c','consommable')], string="Type Produit")
     categorie=fields.Char(string="Categorie")
     categorie_mere=fields.Char(string="Categorie mére")