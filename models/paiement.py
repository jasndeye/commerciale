from email.policy import default
from http import client
from datetime import date
from odoo import models, fields, api

class Paiement(models.TransientModel):
    _name = 'commerciale.paiement'
    
    ref_paiement = fields.Char()
    montant1 = fields.Integer('Montant paiement',default=40)
    type = fields.Selection([('c','Carte Banquaire'),('l','Liquide')], default="l")
    date1 = fields.Date('Date paiement')
    memo1 = fields.Char()
    # facture_id = fields.Many2one('commerciale.facture')
    
    #enregistrer un paiement
    @api.multi
    def action_paiement(self):
        facture=self.env['commerciale.factureclient'].browse(self._context.get('active_ids'))
        for name in facture:
            self.montant1=name.montant
            self.ref_paiement=name.ref_facture
        self.env['commerciale.paiement'].create({'ref_paiement' :  self.ref_paiement, 'montant1' : self.montant1,'type' : self.type, 'date1' : date.today(), 'memo1' : self.ref_paiement})
        
            
    
    
    
    
    
