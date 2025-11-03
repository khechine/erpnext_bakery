import frappe
from erpnext_bakery.install import get_default_warehouse

def execute():
    """Update default warehouse for existing bakery items to the default warehouse"""
    warehouse = get_default_warehouse()

    # Get all bakery items that have a default warehouse different from the current default
    items_to_update = frappe.db.sql("""
        SELECT name
        FROM `tabItem`
        WHERE item_group IN (
            'Pains', 'Viennoiseries', 'Pâtisseries', 'Gâteaux et Entremets',
            'Biscuits et Snacks', 'Boissons et Suppléments', 'Ingrédients', 'Emballages'
        )
        AND (default_warehouse IS NULL OR default_warehouse != %s)
    """, [warehouse], as_dict=True)

    # Update each item's default warehouse
    for item in items_to_update:
        frappe.db.set_value('Item', item.name, 'default_warehouse', warehouse)

    # Update any existing stock ledger entries and bins if they exist
    if items_to_update:
        frappe.db.commit()
        frappe.msgprint(f"Updated default warehouse for {len(items_to_update)} bakery products to '{warehouse}'")

    # Also update POS Profile warehouse if it exists
    pos_profiles = frappe.db.sql("""
        SELECT name
        FROM `tabPOS Profile`
        WHERE warehouse != %s
    """, [warehouse], as_dict=True)

    for pos in pos_profiles:
        frappe.db.set_value('POS Profile', pos.name, 'warehouse', warehouse)

    frappe.db.commit()