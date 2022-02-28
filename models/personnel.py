from odoo import models,fields,api
from datetime import date

class Personnel(models.Model):
     _inherit='res.users'
     _name = 'commerciale.personnel'

     sexe=fields.Selection([('F','Femme'),('M','Masculin')], string="Sexe")
     adresse=fields.Char(string="Adresse", required=True)
     dateNaiss=fields.Date(string="Date de naissance", required=False)
     poste=fields.Selection([('F','cuisinier'),('M','serveur'),('F','caissier'),('M','gerant'),('F','Technicien de surface')], string="Poste Occupé", required=True)
     info_bancaire=fields.Char(string="Compte Bancaire", required=True)