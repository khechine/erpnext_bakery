import frappe

def execute():
    """Update default warehouse for existing bakery items from Stores - ERP to Stores - E"""
    # Get all bakery items that have default warehouse as "Stores - ERP"
    items_to_update = frappe.db.sql("""
        SELECT name
        FROM `tabItem`
        WHERE default_warehouse = 'Stores - ERP' AND item_group IN (
            'Pains', 'Viennoiseries', 'Pâtisseries', 'Gâteaux et Entremets',
            'Biscuits et Snacks', 'Boissons et Suppléments', 'Ingrédients', 'Emballages'
        )
    """, as_dict=True)

    # Update each item's default warehouse
    for item in items_to_update:
        frappe.db.set_value('Item', item.name, 'default_warehouse', 'Stores - E')

    # Update any existing stock ledger entries and bins if they exist
    if items_to_update:
        frappe.db.commit()
        frappe.msgprint(f"Mis à jour l'entrepôt par défaut pour {len(items_to_update)} produits de boulangerie de 'Stores - ERP' vers 'Stores - E'")

    # Also update POS Profile warehouse if it exists
    pos_profiles = frappe.db.sql("""
        SELECT name
        FROM `tabPOS Profile`
        WHERE warehouse = 'Stores - ERP'
    """, as_dict=True)

    for pos in pos_profiles:
        frappe.db.set_value('POS Profile', pos.name, 'warehouse', 'Stores - E')

    frappe.db.commit()