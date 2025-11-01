import frappe

def execute():
    """Add Bakery POS Profile if it doesn't exist"""
    if not frappe.db.exists("POS Profile", "Bakery POS"):
        pos_profile = frappe.get_doc({
            "doctype": "POS Profile",
            "pos_profile_name": "Bakery POS",
            "company": "ERP",
            "warehouse": "Stores - E",
            "customer": "Walk-in Customer",
            "country": "Tunisia",
            "currency": "TND",
            "write_off_account": "Write Off - ERP",
            "write_off_cost_center": "Main - ERP",
            "account_for_change_amount": "Cash - ERP",
            "cost_center": "Main - ERP",
            "income_account": "Sales - ERP",
            "expense_account": "Cost of Goods Sold - ERP",
            "taxes_and_charges": "TVA 19% - ERP",
            "letter_head": "Standard",
            "print_format": "Standard"
        })

        # Add item groups
        item_groups = ["Pains", "Viennoiseries", "Pâtisseries", "Gâteaux et Entremets", "Biscuits et Snacks", "Boissons et Suppléments"]
        for group in item_groups:
            pos_profile.append("item_groups", {"item_group": group})

        pos_profile.insert(ignore_permissions=True)
        frappe.db.commit()