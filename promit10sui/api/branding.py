import frappe
import frappe.apps
import frappe.utils.change_log

APP_TITLE_OVERRIDES = {
	"frappe": "Promittens",
	"erpnext": "PromittensERP",
	"hrms": "Promittens HR",
}


@frappe.whitelist()
def get_apps():
	"""Wraps frappe.apps.get_apps (the /apps screen + app-switcher data source).
	It re-reads each app's own hooks.py title directly, so the app_data boot
	override in boot.py doesn't reach it — rewrite the same entries here too.
	"""
	apps = frappe.apps.get_apps()
	for app in apps:
		override = APP_TITLE_OVERRIDES.get(app.get("name"))
		if override:
			app["title"] = override
	return apps


@frappe.whitelist()
def get_versions():
	"""Wraps frappe.utils.change_log.get_versions (the Help > About dialog's
	installed-apps list). Same issue as get_apps: reads hooks.py directly.
	"""
	versions = frappe.utils.change_log.get_versions()
	for app_name, override in APP_TITLE_OVERRIDES.items():
		if app_name in versions:
			versions[app_name]["title"] = override
	return versions
