app_name = "erpnext_bakery"
app_title = "ERPNext Bakery"
app_publisher = "Your Name"
app_description = "Bakery module for ERPNext"
app_email = "your@email.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_bakery/css/erpnext_bakery.css"
# app_include_js = "/assets/erpnext_bakery/js/erpnext_bakery.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_bakery/css/erpnext_bakery.css"
# web_include_js = "/assets/erpnext_bakery/js/erpnext_bakery.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext_bakery/public/scss/website"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "erpnext_bakery.utils.jinja_methods",
# 	"filters": "erpnext_bakery.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erpnext_bakery.install.before_install"
after_install = "erpnext_bakery.install.after_install"

# Fixtures
# --------

fixtures = [
    "Item Group",
    "Item",
    "BOM",
    "Supplier",
    "POS Profile"
]

# Uninstallation
# ------------

# before_uninstall = "erpnext_bakery.uninstall.before_uninstall"
# after_uninstall = "erpnext_bakery.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_bakery.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"erpnext_bakery.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_bakery.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_bakery.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_bakery.tasks.weekly"
# 	],
# 	"monthly": [
# 		"erpnext_bakery.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_bakery.install.before_tests"

# Overriding Methods
# ------------------------------
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_bakery.event.get_events"
# }
#
# each overriding function accepts a `data` parameter;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task" : "erpnext_bakery.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# automatically notifiy on any change in these doctypes
# watch_docs = ["Item"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "User",
# 		"filter_by": "owner",
# 		"fields": [],
# 		"partial": 1,
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"erpnext_bakery.auth.validate"
# ]