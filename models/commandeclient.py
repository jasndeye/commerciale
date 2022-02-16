from odoo import models,fields,api

class Commandeclient(models.Model):
     _inherit = 'sale.order'
     _name='commerciale.commandeclient'
     
     description=fields.Text()