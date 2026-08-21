import frappe


def boot_session(bootinfo):
	"""Runs on every login (frappe.boot). Pushes theme/branding info to the
	client so promit10sui.js can render the custom navbar/login logo, title
	and favicon without an extra round trip.

	Docs: https://frappeframework.com/docs/user/en/python-api/hooks#extend_bootinfo
	"""
	bootinfo.promit10sui = {
		"app_title": "Promittens Technologies",
		"logo": "/assets/promit10sui/images/logo-navbar.png",
		"icon": "/assets/promit10sui/images/icon-64.png",
		"favicon": "/assets/promit10sui/images/favicon.ico",
		"colors": {
			"primary": "#1F6FA8",
			"primary_dark": "#124A73",
			"accent": "#25A6E0",
			"ink": "#141922",
			"secondary_text": "#5F5E5A",
			"muted_text": "#888780",
			"border": "#E9ECF0",
			"border_soft": "#EDF1F5",
			"sidebar_bg": "#F7F9FB",
		},
	}

	# The navbar app icon (top-left) is read from bootinfo.app_data — one entry
	# per installed app (frappe, erpnext, promit10sui), keyed by whichever app
	# is currently active (frappe.current_app). Only promit10sui's own entry
	# had app_logo_url set via hooks.py, so viewing an ERPNext page (the common
	# case) fell back to nothing and rendered Frappe's generic default icon.
	# Forcing every entry to our icon here fixes it regardless of which app
	# context is active, and survives Desk's SPA route changes since Frappe
	# re-reads this same list on every navigation rather than re-fetching it.
	app_title_overrides = {
		"erpnext": "PromittensERP",
		"hrms": "Promittens HR",
	}
	for app in bootinfo.get("app_data", []):
		app["app_logo_url"] = "/assets/promit10sui/images/icon-64.png"
		override = app_title_overrides.get(app.get("app_name"))
		if override:
			app["app_title"] = override
