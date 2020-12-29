# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "Vincenziana ammissioni custom",
    'version': "1.0.0.0",
    'author': "AIR-sc",
    'summary': 'Modifica del pulsante di creazione contatto dal modulo ammissione',
    'description' : 'Modifica del pulsante di creazione contatto dal modulo ammissione',
    'license':'OPL-1',
    'category': "Extra Tools",
    'data':[
             'views/contact_form_custom_fields.xml',
             'security/ir.model.access.csv',
             ],
    'website': 'https://www.air-srl.com',
    'depends': ['hr_recruitment'],
    'installable': True,
    'auto_install': False,
	#"images":['static/description/karakorumLogo.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
