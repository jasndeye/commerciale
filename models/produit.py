from odoo import models,fields,api

class Produit(models.Model):
     _name = 'commerciale.produit'
     
     name = fields.Char()
     prix= fields.Float()
     cout= fields.Float()
     photo= fields.Binary()
     description= fields.Text()
     quantite_stock=fields.Integer(string="Quantite Stock")
     type=fields.Selection([('s','stockable'),('c','consommable')], string="Type Produit", default="c")
     categorie=fields.Selection([('a','aliment'),('b','boisson')], default="a", string="Categorie")
     # categorie_mere=fields.Many2one(string="Categorie mére")