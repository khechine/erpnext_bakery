import frappe

def execute():
    """Move bakery products stock from Stores - E to Stores - ERP"""

    source_warehouse = "Stores - E"
    target_warehouse = "Stores - ERP"

    # Ensure source warehouse exists
    if not frappe.db.exists("Warehouse", source_warehouse):
        frappe.throw(f"Warehouse {source_warehouse} does not exist")

    # Create target warehouse if it doesn't exist
    if not frappe.db.exists("Warehouse", target_warehouse):
        frappe.get_doc({
            "doctype": "Warehouse",
            "warehouse_name": target_warehouse,
            "company": frappe.db.get_single_value("Global Defaults", "default_company"),
            "is_group": 0
        }).insert(ignore_permissions=True, ignore_if_duplicate=True)
        frappe.db.commit()
        frappe.msgprint(f"Warehouse {target_warehouse} created successfully")

    # Get all bakery item groups
    bakery_item_groups = [
        'Pains', 'Viennoiseries', 'Pâtisseries', 'Gâteaux et Entremets',
        'Biscuits et Snacks', 'Boissons et Suppléments', 'Ingrédients', 'Emballages'
    ]

    # Get all items in bakery item groups that have stock in source warehouse
    items_with_stock = frappe.db.sql("""
        SELECT DISTINCT i.name, b.actual_qty, b.valuation_rate, b.stock_uom
        FROM `tabItem` i
        INNER JOIN `tabBin` b ON i.name = b.item_code
        WHERE i.item_group IN ({})
        AND b.warehouse = %s
        AND b.actual_qty > 0
    """.format(','.join(['%s'] * len(bakery_item_groups))), bakery_item_groups + [source_warehouse], as_dict=True)

    if not items_with_stock:
        frappe.msgprint("No bakery items found with stock in Stores - E")
        return

    # Create a stock entry for material transfer
    stock_entry = frappe.get_doc({
        "doctype": "Stock Entry",
        "stock_entry_type": "Material Transfer",
        "posting_date": frappe.utils.today(),
        "posting_time": frappe.utils.nowtime(),
        "from_warehouse": source_warehouse,
        "to_warehouse": target_warehouse,
        "company": frappe.db.get_single_value("Global Defaults", "default_company")
    })

    for item in items_with_stock:
        stock_entry.append("items", {
            "item_code": item.name,
            "qty": item.actual_qty,
            "uom": item.stock_uom,
            "transfer_qty": item.actual_qty,
            "conversion_factor": 1,
            "basic_rate": item.valuation_rate,
            "amount": item.actual_qty * item.valuation_rate,
            "s_warehouse": source_warehouse,
            "t_warehouse": target_warehouse
        })

    try:
        stock_entry.insert()
        stock_entry.submit()
        frappe.db.commit()
        frappe.msgprint(f"Successfully moved stock for {len(items_with_stock)} bakery items from {source_warehouse} to {target_warehouse}")
    except Exception as e:
        frappe.db.rollback()
        frappe.throw(f"Error transferring stock: {str(e)}")