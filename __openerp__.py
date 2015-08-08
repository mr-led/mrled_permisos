{
    'name': 'MrLed - Permisos',
    'category': 'Accounting',
    'version': '0.1',
    'depends': ['account','base','l10n_ar_invoice'],
    'data': [
        'account_invoice_view.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'qweb': [],
    'installable': True,
}
