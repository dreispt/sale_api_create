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
        # Original values will be forced at the end
        original_vals = dict(vals)
        # Calculate company from User, if not given
        if not vals.get('company_id'):
            user_obj = self.pool['res.users']
            vals['company_id'] = user_obj.browse(
                cr, uid, uid, context=context).company_id.id
        # Calculate Shop from Company, if not given
        if not vals.get('shop_id'):
            shop_obj = self.pool['sale.shop']
            vals['shop_id'] = shop_obj.search(
                cr, uid, [('company_id', '=', vals['company_id'])],
                context=context)[0]
        # Apply onchange_shop_id
        vals.update(
            self.onchange_shop_id(
                cr, uid, [], vals['shop_id'],
                context=context)['value'])
        # Apply onchange_partner_id
        assert vals.get('partner_id'), "Partner is mandatory"
        vals.update(
            self.onchange_partner_id(
                cr, uid, [], vals['partner_id'],
                context=context)['value'])
        # Apply onchange_pricelist_id
        vals.update(
            self.onchange_pricelist_id(
                cr, uid, [], vals['pricelist_id'], [],
                context=context)['value'])
        # Make sure original values are kept
        vals.update(original_vals)
        id = self.create(cr, uid, vals, context=context)
        return id
        # action_button_confirm(cr, uid, ids, context=None)


class sale_order_line(orm.Model):
    _inherit = "sale.order.line"

    def create_api(self, cr, uid, vals, context=None):
        # Original values will be forced at the end
        original_vals = dict(vals)
        order_id = vals['order_id']
        order_obj = self.pool['sale.order']
        order = order_obj.browse(cr, uid, order_id, context=context)
        # Apply product_id_change
        vals.update(
            self.product_id_change(
                cr, uid, [], order.pricelist_id.id,
                vals['product_id'], vals['product_uom_qty'],
                partner_id=order.partner_id.id,
                context=context)['value'])
        # Make sure original values are kept
        vals.update(original_vals)
        id = self.create(cr, uid, vals, context=context)
        return id
