from odoo import models,fields,api

class Commandeclient(models.Model):
     _inherit = 'sale.order'
     
     description=fields.Text()