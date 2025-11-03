import frappe
from erpnext_bakery.install import get_default_warehouse

def execute():
    """Add initial stock to bakery warehouse"""
    warehouse = get_default_warehouse()

    # Only add stock if warehouse exists and is empty
    if frappe.db.exists("Warehouse", warehouse):
        # Check if any stock already exists
        existing_stock = frappe.db.sql("""
            SELECT COUNT(*) as count
            FROM `tabBin`
            WHERE warehouse = %s AND actual_qty > 0
        """, warehouse, as_dict=True)

        if existing_stock[0].count == 0:
            # Add initial stock for key bakery items
            stock_items = [
                ("FARINE_TYPE_55", 1000, 1.50),
                ("LAIT_ENTIER", 1000, 2.20),
                ("SUCRE_SEMOULE", 300, 3.00),
                ("CHOCOLAT_NOIR", 60, 28.00),
                ("FRUITS_FRAIS_MELANGES", 60, 12.00),
                ("EMBALLAGE_PAPIER", 1200, 0.10),
                ("CAFE_ESPRESSO", 200, 2.00),
                ("VANILLE", 30, 15.00),
                ("BEURRE_DOUX", 100, 25.00),
                ("OEUFS", 200, 4.00)
            ]

            for item_code, qty, rate in stock_items:
                if frappe.db.exists("Item", item_code):
                    # Create stock ledger entry
                    frappe.get_doc({
                        "doctype": "Stock Ledger Entry",
                        "item_code": item_code,
                        "warehouse": warehouse,
                        "posting_date": frappe.utils.today(),
                        "posting_time": "10:00:00",
                        "voucher_type": "Stock Entry",
                        "voucher_no": "SE-001",
                        "actual_qty": qty,
                        "qty_after_transaction": qty,
                        "incoming_rate": rate,
                        "valuation_rate": rate,
                        "stock_value": qty * rate,
                        "stock_value_difference": qty * rate,
                        "company": frappe.db.get_single_value("Global Defaults", "default_company"),
                        "fiscal_year": frappe.utils.getdate().year
                    }).insert(ignore_permissions=True)

                    # Update bin
                    frappe.get_doc({
                        "doctype": "Bin",
                        "item_code": item_code,
                        "warehouse": warehouse,
                        "actual_qty": qty,
                        "stock_uom": "Kg" if item_code in ["FARINE_TYPE_55", "SUCRE_SEMOULE", "CHOCOLAT_NOIR", "FRUITS_FRAIS_MELANGES", "BEURRE_DOUX"] else "Unit",
                        "valuation_rate": rate,
                        "stock_value": qty * rate
                    }).insert(ignore_permissions=True)

            frappe.db.commit()