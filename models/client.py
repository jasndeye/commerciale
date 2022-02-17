from email.policy import default
from odoo import models,fields,api

class Client(models.Model):
     _name = 'commerciale.client'
     
     nom = fields.Char(string="Nom", required=True)
     prenom= fields.Char(string="Prenom", required=True)
     telephone= fields.Char(string="Telephone", required=True)
     mail= fields.Char(string="Email", required=False)
     adresse=fields.Char(string="Adresse", required=True)
     info_bancaire=fields.Char(string="Information Bancaire", required=True)
     point_fidelite = fields.Integer(string="Point fidélité" ,default=0)