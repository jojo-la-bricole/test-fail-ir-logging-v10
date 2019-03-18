# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Users(models.Model):
    _name = 'res.users'
    _inherit = ['res.users']

    name2 = fields.Char(string='Name')
    name3 = fields.Char(string='Name')
    name4 = fields.Char(string='Name')
    name5 = fields.Char(string='Name')

    @api.one
    @api.constrains('nonexistingfield')
    def _test(self):
        pass
