from datetime import date
from email.policy import default
from odoo import models,fields,api
from setuptools import Command

class Commandeclient(models.Model):
     _name='commerciale.commandeclient'
     
     #Champs de commande
     client_id=fields.Many2one('commerciale.client', required=True)
     etat_commande = fields.Selection([('b','Brouillon'),('o','Ouvert')], default="b",compute ='_compute_etat')
     vendeur_id = fields.Many2one('commerciale.personnel',)
     montant = fields.Integer('Montant commande')
     date = fields.Date('Date commande')
     detail_ids=fields.One2many('commerciale.detailscommandeclient','commande_id')
     
     #Champs de paiement
     montant1 = fields.Integer('Montant paiement')
     type = fields.Selection([('c','Carte Banquaire'),('l','Liquide')], default="l")
     date1 = fields.Date('Date paiement')
     memo1 = fields.Char('Memo')
     
     #Champs de facture
     ref_facture = fields.Char(default='1')
     
     #appel popup paiement
     @api.multi
     def action_enregistrer_paiement(self):
        view_id=self.env.ref('commerciale.action_enregistrer_paiement').id
        return{
            'name':'Enregistrer paiement',
            'view_mode':'form',
            'views':[[view_id,'form']],
            'res_model':'commerciale.paiement',
            'type':'ir.actions.act_window',
            'target':'new'
            
        }
         
      #enregistrer une facture       
     @api.multi
     def action_facturer(self):
        auts=self.env['commerciale.factureclient']
        cl_p=auts.search_count([])

        dates=date.today()
        refs=str(dates)+"/"+str(int(cl_p)+1)
        self.env['commerciale.factureclient'].create({'ref_facture' :  refs, 'montant' : self.montant,'ref_commande' : refs, 'status' : 'o', 'date' : dates})
        # compter le nombre de factures

        # for f in facture:
            # f.ref_facture=date.day+"/"+1
            # f.ref_facture="test"
            # f.montant = self.montant
            # f.client_id = self.client_id
            # f.vendeur_id = self.vendeur_id
            # f.produit_ids = self.produit_ids
            # f.status= 'o'
            # f.date = self.date
            # self.ref_facture = f.ref_facture

      #changer etat de la commande      
     def _compute_etat(self):
         for var in self:
             var.etat_commande='o'

      #appel popup paiement
     @api.model
     def affiche_factures(self):
        print("#########################################################") 
        # factures=self.env['commerciale.factureclient']
        # print(factures)
        # return factures
     
             
    #attribuer l'etat de la facture au paiement    
    #  def _compute_ref_facture(self):
    #      for var in self:
    #          var.memo = var.ref_facture
             
            

#Les détails de la commande
class Detailscommandeclient(models.Model):
     _name='commerciale.detailscommandeclient'     
           
     produit_id=fields.Many2one('commerciale.produit',string='Nom Produit' ,required=True)
     sous_total = fields.Integer('Montant commande')
     quantite = fields.Integer('Quantité commande')
     prix_unitaire=fields.Float('Prix unitaire')
     commande_id=fields.Many2one('commerciale.commandeclient','detail_ids')