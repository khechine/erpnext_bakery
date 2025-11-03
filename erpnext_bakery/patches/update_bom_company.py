import frappe
from erpnext_bakery.install import get_default_company

def execute():
    """Update BOM company field to use dynamic company"""
    company = get_default_company()
    
    # Update all BOMs to use the detected company
    boms = frappe.db.sql("SELECT name FROM `tabBOM` WHERE name LIKE 'BOM-%'", as_dict=True)
    
    for bom in boms:
        # Update BOM company field if it exists and needs updating
        if frappe.db.exists("BOM", bom.name):
            try:
                # Update the company field
                frappe.db.set_value("BOM", bom.name, "company", company)
                frappe.db.commit()
            except Exception as e:
                # Some BOMs might not have company field, that's ok
                frappe.log_error(f"Could not update company for BOM {bom.name}: {e}")
                frappe.db.rollback()
                continue