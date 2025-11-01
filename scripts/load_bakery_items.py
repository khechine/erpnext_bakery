import frappe
from frappe.utils import flt

def create_item_groups():
    """Create item groups if they don't exist."""
    item_groups = [
        "Pains",
        "Viennoiseries",
        "Pâtisseries",
        "Gâteaux et Entremets",
        "Biscuits et Snacks",
        "Ingrédients",
        "Emballages",
        "Boissons et Suppléments"
    ]

    for group in item_groups:
        if not frappe.db.exists("Item Group", group):
            item_group = frappe.get_doc({
                "doctype": "Item Group",
                "item_group_name": group,
                "parent_item_group": "All Item Groups",
                "is_group": 0
            })
            item_group.insert(ignore_permissions=True)
            frappe.msgprint(f"Created Item Group: {group}")

def create_items():
    """Create items (finished products and ingredients) if they don't exist."""
    items = [
        # Finished Products
        {
            "item_code": "BAGUETTE_TRADITION",
            "item_name": "Baguette Tradition",
            "item_group": "Pains",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 1.20,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "PAIN_COMPLET_500G",
            "item_name": "Pain Complet 500g",
            "item_group": "Pains",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 2.00,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "CROISSANT_BEURRE",
            "item_name": "Croissant Beurre",
            "item_group": "Viennoiseries",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 2.20,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "PAIN_CHOCOLAT",
            "item_name": "Pain au Chocolat",
            "item_group": "Viennoiseries",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 2.50,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "TARTELETTE_FRUITS",
            "item_name": "Tartelette aux Fruits",
            "item_group": "Pâtisseries",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 4.50,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "ECLAIR_CHOCOLAT",
            "item_name": "Éclair au Chocolat",
            "item_group": "Pâtisseries",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 4.00,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "GATEAU_FRAISIER",
            "item_name": "Gâteau Fraisier (6 parts)",
            "item_group": "Gâteaux et Entremets",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 28.00,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "COOKIES_PEPIES",
            "item_name": "Cookies aux Pépites",
            "item_group": "Biscuits et Snacks",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 1.80,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "CAFE_ESPRESSO",
            "item_name": "Café Espresso",
            "item_group": "Boissons et Suppléments",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 2.00,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "CAPPUCCINO",
            "item_name": "Cappuccino",
            "item_group": "Boissons et Suppléments",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 3.50,
            "default_warehouse": "Stores - ERP"
        },
        # Ingredients
        {
            "item_code": "FARINE_TYPE_55",
            "item_name": "Farine Type 55",
            "item_group": "Ingrédients",
            "stock_uom": "Kg",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 1.50,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "LEVURE_BOULANGERE",
            "item_name": "Levure Boulangère",
            "item_group": "Ingrédients",
            "stock_uom": "Kg",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 8.00,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "BEURRE_DOUX",
            "item_name": "Beurre Doux",
            "item_group": "Ingrédients",
            "stock_uom": "Kg",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 25.00,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "SUCRE_SEMOULE",
            "item_name": "Sucre Semoule",
            "item_group": "Ingrédients",
            "stock_uom": "Kg",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 3.00,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "OEUFS",
            "item_name": "Œufs",
            "item_group": "Ingrédients",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 4.00,
            "default_warehouse": "Stores - E"
        },
        {
            "item_code": "LAIT_ENTIER",
            "item_name": "Lait Entier",
            "item_group": "Ingrédients",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 2.20,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "CHOCOLAT_NOIR",
            "item_name": "Chocolat Noir",
            "item_group": "Ingrédients",
            "stock_uom": "Kg",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 28.00,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "FRUITS_FRAIS_MELANGES",
            "item_name": "Fruits Frais Mélangés",
            "item_group": "Ingrédients",
            "stock_uom": "Kg",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 12.00,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "SEL_FIN",
            "item_name": "Sel Fin",
            "item_group": "Ingrédients",
            "stock_uom": "Kg",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 1.20,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "EMBALLAGE_PAPIER",
            "item_name": "Emballage Papier",
            "item_group": "Emballages",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 0.10,
            "default_warehouse": "Stores - ERP"
        },
        {
            "item_code": "BOITE_GATEAU_6",
            "item_name": "Boîte Gâteau 6 parts",
            "item_group": "Emballages",
            "stock_uom": "Unit",
            "is_stock_item": 1,
            "include_in_price_list": 1,
            "standard_rate": 1.20,
            "default_warehouse": "Stores - ERP"
        }
    ]

    for item_data in items:
        if not frappe.db.exists("Item", item_data["item_code"]):
            item = frappe.get_doc({
                "doctype": "Item",
                **item_data
            })
            item.insert(ignore_permissions=True)
            frappe.msgprint(f"Created Item: {item_data['item_name']}")

def create_boms():
    """Create BOMs for bakery products."""
    boms = [
        {
            "bom_name": "BOM-CROISSANT_BEURRE",
            "item": "CROISSANT_BEURRE",
            "quantity": 1,
            "items": [
                {"item_code": "FARINE_TYPE_55", "qty": 0.1, "uom": "Kg"},
                {"item_code": "BEURRE_DOUX", "qty": 0.02, "uom": "Kg"},
                {"item_code": "SEL_FIN", "qty": 0.001, "uom": "Kg"},
                {"item_code": "LEVURE_BOULANGERE", "qty": 0.005, "uom": "Kg"},
                {"item_code": "LAIT_ENTIER", "qty": 0.02, "uom": "Unit"},
                {"item_code": "OEUFS", "qty": 0.1, "uom": "Unit"}
            ]
        },
        {
            "bom_name": "BOM-BAGUETTE_TRADITION",
            "item": "BAGUETTE_TRADITION",
            "quantity": 1,
            "items": [
                {"item_code": "FARINE_TYPE_55", "qty": 0.3, "uom": "Kg"},
                {"item_code": "SEL_FIN", "qty": 0.006, "uom": "Kg"},
                {"item_code": "LEVURE_BOULANGERE", "qty": 0.01, "uom": "Kg"},
                {"item_code": "LAIT_ENTIER", "qty": 0.05, "uom": "Unit"}
            ]
        },
        {
            "bom_name": "BOM-TARTELETTE_FRUITS",
            "item": "TARTELETTE_FRUITS",
            "quantity": 1,
            "items": [
                {"item_code": "FARINE_TYPE_55", "qty": 0.1, "uom": "Kg"},
                {"item_code": "BEURRE_DOUX", "qty": 0.05, "uom": "Kg"},
                {"item_code": "SUCRE_SEMOULE", "qty": 0.02, "uom": "Kg"},
                {"item_code": "OEUFS", "qty": 0.2, "uom": "Unit"},
                {"item_code": "FRUITS_FRAIS_MELANGES", "qty": 0.1, "uom": "Kg"}
            ]
        }
    ]

    for bom_data in boms:
        if not frappe.db.exists("BOM", bom_data["bom_name"]):
            bom = frappe.get_doc({
                "doctype": "BOM",
                "bom_name": bom_data["bom_name"],
                "item": bom_data["item"],
                "quantity": bom_data["quantity"],
                "uom": "Unit",
                "is_active": 1,
                "is_default": 1,
                "items": bom_data["items"]
            })
            bom.insert(ignore_permissions=True)
            frappe.msgprint(f"Created BOM: {bom_data['bom_name']}")

def load_bakery_items():
    """Main function to load all bakery items."""
    create_item_groups()
    create_items()
    create_boms()
    frappe.msgprint("All bakery items loaded successfully!")

def reset_bakery_items():
    """Reset all created bakery items for testing."""
    # Delete BOMs first to avoid dependencies
    boms = [
        "BOM-CROISSANT_BEURRE",
        "BOM-BAGUETTE_TRADITION",
        "BOM-TARTELETTE_FRUITS"
    ]
    for bom in boms:
        if frappe.db.exists("BOM", bom):
            frappe.delete_doc("BOM", bom)
            frappe.msgprint(f"Deleted BOM: {bom}")

    # Delete items
    items = [
        "BAGUETTE_TRADITION", "PAIN_COMPLET_500G", "CROISSANT_BEURRE", "PAIN_CHOCOLAT",
        "TARTELETTE_FRUITS", "ECLAIR_CHOCOLAT", "GATEAU_FRAISIER", "COOKIES_PEPIES",
        "CAFE_ESPRESSO", "CAPPUCCINO", "FARINE_TYPE_55", "LEVURE_BOULANGERE",
        "BEURRE_DOUX", "SUCRE_SEMOULE", "OEUFS", "LAIT_ENTIER", "CHOCOLAT_NOIR",
        "FRUITS_FRAIS_MELANGES", "SEL_FIN", "EMBALLAGE_PAPIER", "BOITE_GATEAU_6"
    ]
    for item in items:
        if frappe.db.exists("Item", item):
            frappe.delete_doc("Item", item)
            frappe.msgprint(f"Deleted Item: {item}")

    # Delete item groups
    item_groups = [
        "Pains", "Viennoiseries", "Pâtisseries", "Gâteaux et Entremets",
        "Biscuits et Snacks", "Ingrédients", "Emballages", "Boissons et Suppléments"
    ]
    for group in item_groups:
        if frappe.db.exists("Item Group", group):
            frappe.delete_doc("Item Group", group)
            frappe.msgprint(f"Deleted Item Group: {group}")

    frappe.msgprint("All bakery items reset successfully!")

# Execute the main function
if __name__ == "__main__":
    load_bakery_items()