// Promittens Technologies — Desk theme client script.
// Runs on every Desk page load. Reads the branding block pushed by
// promit10sui.boot.boot_session and applies what CSS can't reach directly
// (favicon swap, navbar logo src, document title).
frappe.provide("promit10sui");

// Navbar app icon itself is fixed server-side now (promit10sui.boot forces
// every bootinfo.app_data[] entry's app_logo_url — that's what Frappe's
// navbar actually renders from, keyed by whichever app is currently active).
// This just handles favicon/title, which are one-time client-side concerns.
$(document).on("app_ready", function () {
	const theme = frappe.boot.promit10sui;
	if (!theme) return;

	if (theme.app_title) {
		frappe.boot.app_name = theme.app_title;
	}

	let favicon = document.querySelector("link[rel~='icon']");
	if (!favicon) {
		favicon = document.createElement("link");
		favicon.rel = "icon";
		document.head.appendChild(favicon);
	}
	favicon.href = theme.favicon;
});

// Desktop home grid: Frappe's own desktop_icon.html only renders an icon +
// title, no description. desktop.js fires a "desktop_screen" event every
// time the grid (re)renders (hide/unhide, folder open, page revisit) — hook
// that instead of a one-time page-load listener, or descriptions vanish the
// next time the grid redraws.
const PT_DESKTOP_ICON_DESCRIPTIONS = {
	Framework: "Developer tools, custom apps and site build settings.",
	Organization: "Company structure, departments and internal settings.",
	"Promittens CRM": "Leads, deals and customer relationships.",
	Accounting: "Chart of accounts, invoicing, payments and financial reports.",
	Assets: "Track and depreciate company assets.",
	Buying: "Purchase orders, suppliers and procurement.",
	Manufacturing: "Production plans, work orders and bill of materials.",
	Projects: "Tasks, timesheets and project tracking.",
	Quality: "Quality inspections and procedures.",
	Selling: "Quotations, sales orders and customers.",
	Stock: "Inventory, warehouses and stock movement.",
	Subcontracting: "Outsourced manufacturing orders.",
	"Promittens Settings": "Company, tax and system-wide ERP settings.",
	"Promittens HR": "Employees, leave, payroll and attendance.",
};

function pt_add_desktop_icon_descriptions() {
	document.querySelectorAll(".desktop-icon .icon-title").forEach((titleEl) => {
		const caption = titleEl.closest(".icon-caption");
		if (!caption || caption.querySelector(".pt-icon-desc")) return; // already added

		const label = titleEl.getAttribute("data-original-title") || titleEl.textContent.trim();
		const description = PT_DESKTOP_ICON_DESCRIPTIONS[label];
		if (!description) return;

		const desc = document.createElement("div");
		desc.className = "pt-icon-desc";
		desc.textContent = description;
		caption.appendChild(desc);
	});
}

$(document).on("desktop_screen", function () {
	// desktop.js finishes wiring up the grid synchronously before this fires,
	// but tooltips/labels are set in the same tick — a micro-delay avoids a
	// race where our div gets read before class names settle.
	setTimeout(pt_add_desktop_icon_descriptions, 0);
});

// Login page: swap logo (page renders before frappe.boot is populated) and
// add the "Powered by" footer. Leading icons and input styling are handled
// in CSS — login.html already ships .field-icon markup, no need to inject it.
$(function () {
	if (!window.location.pathname.includes("/login")) return;

	document.querySelectorAll(".login-content .app-logo").forEach((img) => {
		img.src = "/assets/promit10sui/images/logo-navbar.png";
		img.alt = "Promittens Technologies";
	});

	document.querySelectorAll(".for-login .login-content .page-card-actions").forEach((el) => {
		if (el.querySelector(".pt-login-footer")) return;
		const footer = document.createElement("p");
		footer.className = "pt-login-footer";
		footer.textContent = "Powered by Promittens Technologies";
		el.appendChild(footer);
	});
});
