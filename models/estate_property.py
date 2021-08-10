from odoo import fields, models

class Property(models.Model):
    _inherit = "estate.property"


    def action_sold(self):
        print("i work :)")
        journal = self.env['account.invoice'].create({'partner_id': self.buyer_id.id, 'move_type':'out_invoice', 'journal_id': 0})
        # journal = self.env['account.move'].with_context(default_move_type='out_invoice', partner_id=self.buyer_id.id)._get_default_journal()
        
