from odoo import models,fields,api

class Factureclient(models.Model):
     _name='commerciale.factureclient'
     
     ref_facture = fields.Char()
     montant = fields.Integer('Montant facture')
     ref_commande = fields.Char()
     status = fields.Selection([('o','Ouvert'),('p','Paye')], default="o")
     # ref_commande = fields.Many2one('commerciale.commandeclient')
     date = fields.Date('Date Facturation')
     