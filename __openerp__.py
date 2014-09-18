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

{
    'name': 'Create Sales Order API',
    'author': 'Daniel Reis',
    'version': '7.0',
    'description': """\
Sales Order method to simplify creation through the API.

First, call Sales Order ``create_api``, with same parameters as a standard
create(). You might want to pass values at least for: shop_id, partner_id.

Second, call a Sales Order Line ``create_api`` for each line.
You should pass values for, at least: order_id, product_id, product_uom_qty.
""",
    'category': 'Sales Management',
    'website': 'https://github.com/dreispt',
    'depends': ['sale'],
    'test': ['test.yml'],
    'installable': True,
}
