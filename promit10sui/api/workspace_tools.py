import frappe


@frappe.whitelist()
def set_workspace_visibility(workspace_names, hidden=1):
	"""Show/hide one or more stock Workspaces from the Desk sidebar.

	Deliberately NOT wired into hooks.py as an automatic patch: hiding
	default ERPNext workspaces (Accounts, Selling, Buying, Stock, etc.)
	is a site-specific, reviewable decision, not something that should
	happen silently on `bench migrate`.

	Usage (bench console or Server Script, run once, after review):
		frappe.call(
			"promit10sui.api.workspace_tools.set_workspace_visibility",
			workspace_names=["Home", "Tools", "Users"],
			hidden=1,
		)

	Args:
		workspace_names (list[str] | str): Workspace doc names to update.
		hidden (int): 1 to hide, 0 to restore visibility.
	"""
	frappe.only_for("System Manager")

	if isinstance(workspace_names, str):
		workspace_names = frappe.parse_json(workspace_names)

	updated = []
	for name in workspace_names:
		if not frappe.db.exists("Workspace", name):
			continue
		frappe.db.set_value("Workspace", name, "is_hidden", int(hidden))
		updated.append(name)

	frappe.clear_cache()
	return {"updated": updated, "hidden": int(hidden)}


@frappe.whitelist()
def list_workspaces():
	"""Quick reference: names + current visibility of every workspace on
	this site, so you know what to pass into set_workspace_visibility."""
	frappe.only_for("System Manager")
	return frappe.get_all(
		"Workspace",
		fields=["name", "label", "module", "public", "is_hidden"],
		order_by="module, label",
	)
