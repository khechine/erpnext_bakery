import frappe
from erpnext_bakery.install import get_default_company, get_default_warehouse

def execute():
    """Add Bakery POS Profile if it doesn't exist"""
    if not frappe.db.exists("POS Profile", "Bakery POS"):
        company = get_default_company()
        warehouse = get_default_warehouse()

        pos_profile = frappe.get_doc({
            "doctype": "POS Profile",
            "pos_profile_name": "Bakery POS",
            "company": company,
            "warehouse": warehouse,
            "customer": "Walk-in Customer",
            "country": "United States",
            "currency": "USD",
            "write_off_account": "Write Off",
            "write_off_cost_center": "Main",
            "account_for_change_amount": "Cash",
            "cost_center": "Main",
            "income_account": "Sales",
            "expense_account": "Cost of Goods Sold",
            "letter_head": "Standard",
            "print_format": "Standard"
        })

        # Add item groups
        item_groups = ["Pains", "Viennoiseries", "Pâtisseries", "Gâteaux et Entremets", "Biscuits et Snacks", "Boissons et Suppléments"]
        for group in item_groups:
            pos_profile.append("item_groups", {"item_group": group})

        pos_profile.insert(ignore_permissions=True)
        frappe.db.commit()