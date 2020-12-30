from odoo import api,  fields, models, _
from odoo.exceptions import UserError

class hr_applicant_create_contact(models.Model):
    _inherit = 'hr.applicant'

    # NEI MODULI CHE EREDITANO NON SPECIFICARE IL NOME E LA DESCRIPTION...
    #_name = 'vincenziana.createcontact'
    #_description = 'Crea il contatto'

    #@api.multi
    def create_res_partner_only(self):
        """ Create only partner from the hr.applicants """
        partner_id = 0
        for applicant in self:
            if applicant.partner_id:
                partner_id = applicant.partner_id
                contact_name = applicant.partner_id.name_get()[0][1]
                raise UserError(_('Questo contatto esiste già: ' + contact_name))
            else :
                new_partner_id = self.env['res.partner'].create({
                    'is_company': False,
                    'name': applicant.partner_name,
                    'email': applicant.email_from,
                    'phone': applicant.partner_phone,
                    'mobile': applicant.partner_mobile
                })
                partner_id = new_partner_id.id
                applicant.write({'partner_id': partner_id})

        # partner_action = self.env.ref('base.view_partner_form')
        # dict_act_window = partner_action.read([])[0]
        # dict_act_window['context'] = {'form_view_initial_mode': 'edit'}
        # dict_act_window['res_id'] = partner_id
        # return dict_act_window
