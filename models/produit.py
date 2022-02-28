from odoo import models,fields,api

class Produit(models.Model):
     _name = 'commerciale.produit'
     
     name = fields.Char(required=True)
     prix= fields.Integer(required=True)
     cout= fields.Integer()
     photo= fields.Binary(required=True)
     description= fields.Text()
     quantite_stock=fields.Integer(string="Quantite Stock",required=True)
     type=fields.Selection([('s','stockable'),('c','consommable')], string="Type Produit", default="c")
     categorie=fields.Selection([('a','aliment'),('b','boisson')], default="a", string="Categorie")
     # categorie_mere=fields.Many2one(string="Categorie mére")