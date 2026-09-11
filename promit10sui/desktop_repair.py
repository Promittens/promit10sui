"""Targeted repair for the confirmed orphan desktop parents on production."""

import frappe


def repair_orphan_parents():
	"""Run with bench execute; preserves hidden flags, roles and saved layouts."""
	changes = []
	if not frappe.db.exists("Desktop Icon", "Promittens"):
		for label in ("Assets", "Buying", "Projects", "Selling", "Stock"):
			name = frappe.db.get_value(
				"Desktop Icon",
				{"label": label, "app": "erpnext", "parent_icon": "Promittens"},
				"name",
			)
			if name:
				frappe.db.set_value("Desktop Icon", name, "parent_icon", "")
				changes.append({"name": name, "old_parent": "Promittens", "new_parent": ""})

	if not frappe.db.exists("Desktop Icon", "Promittens HR") and frappe.db.exists(
		"Desktop Icon", {"app": "hrms", "parent_icon": "Promittens HR"}
	):
		folder = frappe.get_doc({
			"doctype": "Desktop Icon",
			"label": "Promittens HR",
			"icon_type": "Folder",
			"app": "hrms",
			"standard": 1,
			"hidden": 0,
			"parent_icon": "",
			"logo_url": "/assets/promit10sui/images/prommittensicon.png",
		})
		folder.insert(ignore_permissions=True)
		changes.append({"created_folder": folder.name})

	if changes:
		frappe.cache.delete_key("desktop_icons")
		frappe.clear_cache()
		frappe.db.commit()
	return {"changes": changes}
