from odoo import models,fields,api

class Factureclient(models.Model):
     _name='commerciale.factureclient'
     
     #champs de facture
     ref_facture = fields.Char()
     montant = fields.Integer('Montant facture')
     ref_commande = fields.Char()
     nom_agent = fields.Many2one('res.users',default=lambda self: self.env.user)
     status = fields.Selection([('o','Ouvert'),('p','Paye')], default="o")
     date = fields.Date('Date Facturation')
     