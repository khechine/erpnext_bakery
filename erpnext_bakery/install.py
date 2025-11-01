import frappe
from frappe import _

def after_install():
    """Load bakery items after app installation"""
    frappe.msgprint(_("Installing ERPNext Bakery - Loading bakery products..."))

    # Load all fixtures automatically (already handled by fixtures in hooks.py)
    frappe.msgprint(_("Bakery products loaded successfully!"))

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