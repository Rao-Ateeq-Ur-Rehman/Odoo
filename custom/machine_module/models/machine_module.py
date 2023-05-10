from odoo import models, api, fields

class MachineDetails(models.Model):
    _name = "machine.data"
    _inherit = ["mail.thread",'mail.activity.mixin']
    _description = "Machines Data"

    machineName = fields.Char(string='Machine Name', tracking=True)
    ppLotNum = fields.Char(string='PP Lot Num', tracking=True)
    # age = fields.Integer(string='Age' , tracking=True)
    # dept = fields.Char(string='Department' , tracking=True)
    # gender = fields.Selection([('male','Male'),('female','Female')], string='Gender' , tracking=True)
    # active = fields.Boolean(string='Active', default=True , tracking=True)
    # wfh = fields.Boolean(string='Work From Home', default=False , tracking=True)
    # review = fields.Selection([('0','Bad'),('1','Normal'),('2','Good'),('3','Great')], string="Employee Reviews" , tracking=True, default='3')
    #
