// ERPNext Bakery Custom JavaScript

frappe.ui.form.on('Item', {
    refresh: function(frm) {
        // Add custom bakery-specific logic for items
        if (frm.doc.item_group && frm.doc.item_group.match(/Pains|Viennoiseries|Pâtisseries/)) {
            // Add bakery-specific fields or validations
            console.log('Bakery item detected:', frm.doc.item_code);
        }
    }
});

frappe.ui.form.on('BOM', {
    refresh: function(frm) {
        // Add custom logic for bakery BOMs
        if (frm.doc.item && frm.doc.item.match(/(CROISSANT|BAGUETTE|TARTELETTE)/)) {
            console.log('Bakery BOM detected:', frm.doc.name);
        }
    }
});

// Custom POS integration for bakery
$(document).ready(function() {
    // Bakery-specific POS enhancements can be added here
    console.log('ERPNext Bakery JS loaded');
});