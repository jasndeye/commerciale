from email.policy import default
from http import client
from datetime import date
from odoo import models, fields, api

class Paiementclient(models.Model):
    _name = 'commerciale.paiementclient'
    
    ref_paiement = fields.Char()
    montant1 = fields.Integer('Montant paiement',default=40)
    type = fields.Selection([('c','Carte Banquaire'),('l','Liquide')], default="l")
    date1 = fields.Date('Date paiement')
    memo1 = fields.Char()
    # facture_id = fields.Many2one('commerciale.facture')
    
    
            
    
    
    
    
    
