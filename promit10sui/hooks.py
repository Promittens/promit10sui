app_name = "promit10sui"
app_title = "Promittens Technologies"
app_publisher = "Promittens Technologies"
app_description = "Custom Desk theme, branding and navigation for Promittens Technologies"
app_email = "akshaykrish264@gmail.com"
app_license = "mit"

app_logo_url = "/assets/promit10sui/images/icon-64.png"

website_context = {
	"favicon": "/assets/promit10sui/images/favicon.ico",
	"splash_image": "/assets/promit10sui/images/splash.png",
}

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "promit10sui",
# 		"logo": "/assets/promit10sui/logo.png",
# 		"title": "promit10sUI",
# 		"route": "/promit10sui",
# 		"has_permission": "promit10sui.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# NOTE: ?v=N is a manual cache-buster — these are plain files (not esbuild
# bundles), so browsers can hold onto a stale copy indefinitely otherwise.
# Bump N whenever promit10sui.css/js changes.
app_include_css = "/assets/promit10sui/css/promit10sui.css?v=27"
app_include_js = "/assets/promit10sui/js/promit10sui.js?v=27"

# include js, css files in header of web template
web_include_css = "/assets/promit10sui/css/promit10sui.css?v=27"
web_include_js = "/assets/promit10sui/js/promit10sui.js?v=27"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "promit10sui/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "promit10sui/public/icons.svg"

# Boot Session
# ------------------
# push brand tokens (colors, logo paths) to frappe.boot for promit10sui.js
extend_bootinfo = "promit10sui.boot.boot_session"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "promit10sui.utils.jinja_methods",
# 	"filters": "promit10sui.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "promit10sui.install.before_install"
after_install = "promit10sui.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "promit10sui.uninstall.before_uninstall"
# after_uninstall = "promit10sui.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "promit10sui.utils.before_app_install"
# after_app_install = "promit10sui.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "promit10sui.utils.before_app_uninstall"
# after_app_uninstall = "promit10sui.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "promit10sui.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "promit10sui.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"promit10sui.tasks.all"
# 	],
# 	"daily": [
# 		"promit10sui.tasks.daily"
# 	],
# 	"hourly": [
# 		"promit10sui.tasks.hourly"
# 	],
# 	"weekly": [
# 		"promit10sui.tasks.weekly"
# 	],
# 	"monthly": [
# 		"promit10sui.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "promit10sui.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "promit10sui.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"frappe.apps.get_apps": "promit10sui.api.branding.get_apps",
	"frappe.utils.change_log.get_versions": "promit10sui.api.branding.get_versions",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "promit10sui.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["promit10sui.utils.before_request"]
# after_request = ["promit10sui.utils.after_request"]

# Job Events
# ----------
# before_job = ["promit10sui.utils.before_job"]
# after_job = ["promit10sui.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"promit10sui.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

