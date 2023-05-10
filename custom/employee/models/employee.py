from odoo import models, api, fields

class EmployeeDetails(models.Model):
    _name = "employee.data"
    _inherit = ["mail.thread",'mail.activity.mixin']
    _description = "Employees Data"

    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age' , tracking=True)
    dept = fields.Char(string='Department' , tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender' , tracking=True)
    active = fields.Boolean(string='Active', default=True , tracking=True)
    wfh = fields.Boolean(string='Work From Home', default=False , tracking=True)
    review = fields.Selection([('0','Bad'),('1','Normal'),('2','Good'),('3','Great')], string="Employee Reviews" , tracking=True, default='3')

