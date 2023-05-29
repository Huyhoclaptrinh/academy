# -*- coding: utf-8 -*-

from odoo import models, fields


class Teacher(models.Model):
    _name = 'academy.teacher'
    _description = 'encapsulate teachers information in academy'

    name = fields.Char()
    biography = fields.Html()

    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")


class Course(models.Model):
    _inherit = 'product.template'
    _description = 'encapsulate courses information'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teacher', string="Teacher")
    lesson_ids = fields.One2many('academy.lesson', 'course_id', string="Lessons")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Completed'),
        ('cancel', 'Cancelled'), ], 'State', default='draft',
        store=True)

    def do_print_picking(self):
        self.write({'printed': True})
        return self.env.ref('academy.action_report_picking').report_action(self)


class Lesson(models.Model):
    _name = 'academy.lesson'
    _description = 'encapsulate lessons information in academy'

    name = fields.Char()
    predict_amount_hours = fields.Integer()
    course_video = fields.Char()
    referances = fields.Binary(string='Upload References')
    homework = fields.Binary(string='Upload homework')
    course_id = fields.Many2one('product.template', string="Course")




