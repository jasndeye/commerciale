from odoo import models,fields,api

class Commandefournisseur(models.Model):
     _inherit = 'sale.order'
     
     description=fields.Text()