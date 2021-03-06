# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import UserError


class Address(models.Model):
    _inherit = 'clv.mfile'

    state = fields.Selection(
        [('new', 'New'),
         ('getting', 'Getting'),
         ('stored', 'Stored'),
         ('checked', 'Checked'),
         ('in_use', 'In Use'),
         ('used', 'Used'),
         ('deleted', 'Deleted'),
         ], string='State', default='new', readonly=True, required=True
    )

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        return True

    def change_state(self, new_state):
        for mfile in self:
            if mfile.is_allowed_transition(mfile.state, new_state):
                mfile.state = new_state
            else:
                raise UserError('Status transition (' + mfile.state + ', ' + new_state + ') is not allowed!')

    def action_new(self):
        for mfile in self:
            mfile.change_state('new')

    def action_getting(self):
        for mfile in self:
            mfile.change_state('getting')

    def action_stored(self):
        for mfile in self:
            mfile.change_state('stored')

    def action_checked(self):
        for mfile in self:
            mfile.change_state('checked')

    def action_in_use(self):
        for mfile in self:
            mfile.change_state('in_use')

    def action_used(self):
        for mfile in self:
            mfile.change_state('used')

    def action_deleted(self):
        for mfile in self:
            mfile.change_state('deleted')
