import frappe


def after_install():
	"""Idempotent — safe to call on a fresh install (after_install hook) or
	again later via the patch in patches.txt (needed because this app was
	already installed on promittens.local before this theme existed, so the
	hook itself won't refire)."""
	create_organization_workspace()
	set_login_logo()


def create_organization_workspace():
	"""The Workspace itself is defined in the fixture at
	promit10sui/workspace/organization/organization.json — NOT built here via
	the ORM. `bench migrate` runs a core housekeeping patch
	(frappe.model.sync.remove_orphan_entities) that deletes any *public*
	Workspace whose module belongs to an installed app but has no matching
	<module>/workspace/<name>/<name>.json file on disk; an ORM-inserted
	Workspace with nothing backing it on disk gets swept away on the very
	next migrate. frappe.reload_doc reads that fixture and upserts the DB
	record, which is also what keeps it from being treated as orphaned.
	"""
	frappe.reload_doc("promit10sui", "workspace", "organization", force=True)


def set_login_logo():
	"""Point the login page at the Promittens logo. Website Settings.app_logo
	is a separate setting from the app_logo_url hook — the hook only affects
	the Desk navbar, Frappe reads the login-page logo from this DB field."""
	logo_path = "/assets/promit10sui/images/logo-navbar.png"
	current = frappe.db.get_single_value("Website Settings", "app_logo")
	if current == logo_path:
		return
	frappe.db.set_single_value("Website Settings", "app_logo", logo_path)
	frappe.db.commit()
