from odoo import fields, models

class Property(models.Model):
    _inherit = "estate.property"


    def action_sold(self):
        print("i work :)")
        journal = self.env['account.invoice'].create({'partner_id': self.buyer_id.id, 'move_type':'out_invoice', 'journal_id':1, 'account_id': 1,
        "invoice_line_ids": [
                (
                    0,
                    0,
                    {
                        "name": self.name,
                        "quantity": 1,
                        "price_unit": self.selling_price,
                        'account_id': 1,
                        'tax_ids': 0,
                    },
                )
            ],})
        # journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        return super().action_sold()
