from odoo import models,fields,api

class Commande(models.Model):
     _inherit = 'sale.order'
     
     description=fields.Text()