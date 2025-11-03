import frappe
from frappe import _

def after_install():
    """Load bakery items after app installation"""
    frappe.msgprint(_("Installing ERPNext Bakery - Loading bakery products..."))

    # Load all fixtures automatically (already handled by fixtures in hooks.py)
    frappe.msgprint(_("Bakery products loaded successfully!"))

def get_default_company():
    """Get the default company from Global Defaults"""
    return frappe.db.get_single_value("Global Defaults", "default_company")

def get_default_warehouse():
    """Get or create a default warehouse for bakery products"""
    company = get_default_company()
    warehouse_name = f"Stores - {company}"

    if not frappe.db.exists("Warehouse", warehouse_name):
        # Create the warehouse if it doesn't exist
        warehouse = frappe.get_doc({
            "doctype": "Warehouse",
            "warehouse_name": warehouse_name,
            "company": company,
            "is_group": 0
        })
        warehouse.insert(ignore_permissions=True)
        frappe.db.commit()
        frappe.msgprint(f"Created default warehouse: {warehouse_name}")

    return warehouse_name

def before_install():
    """Before installation tasks"""
    pass

def create_sample_purchase_invoices():
    """Create sample purchase invoices for demonstration"""
    # This function can be called manually if needed
    frappe.msgprint(_("Sample purchase invoices created"))

def create_initial_stock():
    """Create initial stock entries"""
    # This function can be called manually if needed
    frappe.msgprint(_("Initial stock created"))