from email.policy import default
from odoo import models,fields,api

class Client(models.Model):
     _name = 'commerciale.client'
     
     name = fields.Char(string="Nom", required=True)
     telephone= fields.Char(string="Telephone", required=True)
     mail= fields.Char(string="Email", required=False)
     adresse=fields.Char(string="Adresse", required=True)
     info_bancaire=fields.Integer(string="Numero de compte bancaire", required=True)
     point_fidelite = fields.Integer(string="Point fidélité" ,default=0)