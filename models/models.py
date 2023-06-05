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


class Lesson(models.Model):
    _name = 'academy.lesson'
    _description = 'encapsulate lessons information in academy'

    name = fields.Char()
    predict_amount_hours = fields.Integer()
    course_video = fields.Char()
    references = fields.Many2many(comodel_name='ir.attachment')
    homework = fields.Binary(string='Upload homework')
    course_id = fields.Many2one('product.template', string="Course")




