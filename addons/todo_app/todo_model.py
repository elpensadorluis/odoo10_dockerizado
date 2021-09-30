from odoo import models, fields


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'ToDo Task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
