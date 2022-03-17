# Copyright (C) 2009  Renato Lima - Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Brazilian Localization Purchase",
    "license": "AGPL-3",
    "category": "Localisation",
    "author": "Akretion, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-brazil",
    "version": "14.0.1.0.0",
    "depends": ["purchase", "l10n_br_account"],
    "data": [
        # Security
        "security/ir.model.access.csv",
        # Data
        "data/company.xml",
        # View
        "views/purchase_view.xml",
        "views/res_company_view.xml",
        # Reports
        "reports/purchase_report_views.xml",
        "reports/purchase_order_templates.xml",
    ],
    "installable": True,
    "post_init_hook": "post_init_hook",
    "auto_install": False,
}
