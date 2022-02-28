from email.policy import default
from http import client
from datetime import date
from odoo import models, fields, api

class Paiement(models.TransientModel):
    _name = 'commerciale.paiement'
    
    #recuper le montant de la commande concernee
    @api.model 
    def _compute_montant(self):
        facture=self.env['commerciale.commandeclient'].browse(self._context.get('active_ids'))
        for name in facture:
            return name.montant 
              

    #Champs de paiement
    ref_paiement = fields.Char()
    montant1 = fields.Integer('Montant paiement', default=_compute_montant)
    type = fields.Selection([('c','Carte Banquaire'),('l','Liquide')], default="l")
    date1 = fields.Date('Date paiement')
    memo1 = fields.Char('Ref Facture')
    nom_agent = fields.Many2one('res.users',default=lambda self: self.env.user)

    
    #enregistrer un paiement
    @api.multi
    def action_paiement(self):

        #recuperer la commande concernee
        refcommande=""
        commande=self.env['commerciale.commandeclient'].browse(self._context.get('active_ids'))
        for name in commande:
            refcommande= name.ref_commande
            point=name.client_id.point_fidelite+1

            #incrementer les points de fidelite
            rf=str(name.client_id.id)
            pt=str(point)
            ats="update commerciale_client set point_fidelite="+pt+" where id = "+rf
            self.env.cr.execute(ats)    

        #recuperer la facture concernee    
        facture=self.env['commerciale.factureclient'].search([('ref_commande','=',refcommande)]) 
        for name in facture:
            self.montant1=name.montant
            self.ref_paiement=name.ref_facture

        #renseigner le reste des champs de paiement le paiement 

        self.memo1=self.ref_paiement
        self.date1=date.today()

        #changer etat de la facture  
        
        rf="'"+name.ref_facture+"'"
        ats="update commerciale_factureclient set status='p' where ref_facture = "+rf
        self.env.cr.execute(ats)
       
    
    
    
    
    
