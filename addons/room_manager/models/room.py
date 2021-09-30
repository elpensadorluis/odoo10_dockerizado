from odoo import models, fields


class Room(models.Model):
    _name = 'room'
    _description = 'Room Manager'
    name = fields.Char('Room Name', required=True)
    active = fields.Boolean('Active?', default=True)
    description = fields.Char('Active Description')


class RoomAssign(models.Model):
    _name = 'room.assign'
    _description = 'Assign Room'
    in_room = fields.Many2one('room', 'Room')
    customer = fields.Many2one('res.partner', 'Customer')
    from_ = fields.Date('From')
    to_ = fields.Date('To')
    personal_id = fields.Many2many('hr.employee', string='Employees')
    equipments = fields.Many2many('product.template', string='Equipments')
