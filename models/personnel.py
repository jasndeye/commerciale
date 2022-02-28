from odoo import models,fields,api
from datetime import date

class Personnel(models.Model):
     _name = 'commerciale.personnel'

     nom = fields.Char(string="Nom" , required=True)
     prenom= fields.Char(string="Prenom", required=True)
     telephone= fields.Char(string="Telephone", required=True)
     sexe=fields.Selection([('F','Femme'),('M','Masculin')], string="Sexe")
     mail= fields.Char(string="Email")
     adresse=fields.Char(string="Adresse", required=True)
     dateNaiss=fields.Date(string="Date de naissance", required=False)
     poste=fields.Selection([('F','cuisinier'),('M','serveur'),('F','caissier'),('M','gerant'),('F','Technicien de surface')], string="Poste Occupé", required=True)
     info_bancaire=fields.Char(string="Compte Bancaire", required=True)