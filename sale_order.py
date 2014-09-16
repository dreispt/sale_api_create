# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm


class sale_order(orm.Model):
    _inherit = "sale.order"

    def create_api(self, cr, uid, vals, context=None):
        """
        company_id
        partner_id
        completion_date
        """

        if not vals.get('company_id'):
            user_obj = self.pool['res.users']
            vals['company_id'] = user_obj.browse(
                cr, uid, uid, context=context).company_id.id
        if not vals.get('shop_id'):
            shop_obj = self.pool['sale.shop']
            vals['shop_id'] = shop_obj.search(
                cr, uid, [('company_id', '=', vals['company_id'])],
                context=context)[0]
        # onchange shop_id
        vals.update(
            self.onchange_shop_id(
                cr, uid, [], vals['shop_id'], context=context)['value'])
        #def onchange_partner_id(self, cr, uid, ids, part, context=None):
        #def onchange_pricelist_id(self, cr, uid, ids, pricelist_id, order_lines, context=None):
        print vals
        id = self.create(cr, uid, vals, context=context)
        return id
