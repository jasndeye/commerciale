from datetime import date
from email.policy import default
from odoo import models,fields,api
from setuptools import Command

class Commandeclient(models.Model):
     _name='commerciale.commandeclient'
     
     #Champs de commande
     ref_commande= fields.Char()
     client_id=fields.Many2one('commerciale.client', required=True)
     etat_commande = fields.Selection([('b','Brouillon'),('o','Ouvert')], default="b",compute ='_compute_etat')
     nom_agent = fields.Char('Caissier')
     montant = fields.Integer('Montant Total')
     detail_ids=fields.One2many('commerciale.detailscommandeclient','commande_id')
     date = fields.Date(compute='_compute_date')
     
     #Champs de paiement
     montant1 = fields.Integer('Montant paiement')
     type = fields.Selection([('c','Carte Banquaire'),('l','Liquide')], default="l")
     date1 = fields.Date('Date paiement')
     memo1 = fields.Char('Memo')
     
     #Champs de facture
     ref_facture = fields.Char()
     
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
           # compter le nombre de factures
        auts=self.env['commerciale.factureclient']
        cl_p=auts.search_count([])

        dates=date.today()
        refs=str(dates)+"/"+str(int(cl_p)+1)
        fn=self.env['commerciale.factureclient'].create({'ref_facture' :refs, 'montant' :self.montant,'ref_commande' : refs, 'status' : 'o', 'date' : dates}) 
        if fn:
             rf="'"+refs+"'"
             ats="update commerciale_commandeclient set etat_commande='o' where ref_commande = "+rf
             self.env.cr.execute(ats) 
       
      
     #afficher facture
    #  @api.multi
    #  def action_paiement(self):
        # facture=self.env['commerciale.factureclient'].browse(self._context.get('active_ids'))
        # for name in facture:
        #     self.montant1=name.montant
        #     self.journal1=name.journal
        # print("ôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôôô")
        # self.env['commerciale.paiement'].create({'ref_paiement' :  self.ref_paiement, 'montant1' : self.montant,'journal1' : self.journal, 'date1' : date.today, 'memo' : self.memo})
        # print("###################################################test##############################") 

      #changer etat de la commande      
     def _compute_etat(self):
         for var in self:
             var.etat_commande='o'

     #date de la commande      
     def _compute_date(self):
         for var in self:
             var.date=date.today()       

      #charger automatiquement le montant  
     @api.onchange('detail_ids') 
     def _compute_montant(self):
          mont=0
          for var in self :
               if var.detail_ids :
                    for i in var.detail_ids:
                         mont+=i.sous_total
               var.montant=mont
               var.montant1=mont  
     
             
    #attribuer l'etat de la facture au paiement    
     def _compute_ref_facture(self):
         for var in self:
             var.memo = var.ref_facture
            

#Les détails de la commande
class Detailscommandeclient(models.Model):
     _name='commerciale.detailscommandeclient'     
           
     produit_id=fields.Many2one('commerciale.produit',string='Nom Produit' ,required=True)
     sous_total = fields.Integer('Sous total',compute='_compute_s_total')
     quantite = fields.Integer('Quantité commande')
     prix_unitaire=fields.Integer('Prix unitaire')
     commande_id=fields.Many2one('commerciale.commandeclient','detail_ids')
    

     #charger automatiquement le sous-total
     @api.onchange('prix_unitaire','quantite')     
     def _compute_s_total(self):
         for var in self:
             var.sous_total=var.quantite*var.prix_unitaire
