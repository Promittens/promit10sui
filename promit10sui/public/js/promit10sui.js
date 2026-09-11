// Promittens Technologies — Desk theme client script.
// Runs on every Desk page load. Reads the branding block pushed by
// promit10sui.boot.boot_session and applies what CSS can't reach directly
// (favicon swap, navbar logo src, document title).
frappe.provide("promit10sui");

// Filter the desktop profile menu before Frappe creates its menu instance.
const pt_create_menu = frappe.ui.create_menu;
frappe.ui.create_menu = function (opts) {
	if ($(opts.parent).is(".desktop-avatar")) {
		opts = {
			...opts,
			menu_items: opts.menu_items.filter((item) => item.label !== "Frappe Support"),
		};
	}
	return pt_create_menu.call(this, opts);
};

// Frappe emits this document event after the dialog is attached and shown.
// Bootstrap's earlier show event can fire while the wrapper is detached.
$(document).on("frappe.ui.Dialog:shown", function () {
	const dialog = frappe.ui.misc?.about_dialog;
	if (!dialog) return;
	$(dialog.wrapper).find(".about-frappe-wordmark").attr({
		src: "/assets/promit10sui/images/prommittensLOGO.png",
		alt: "Prommittens Technologies",
	}).css({ height: "64px", width: "auto", maxWidth: "100%", objectFit: "contain", filter: "none" });
	$(dialog.wrapper).find(".about-footer").text("© Prommittens Technologies Pvt. Ltd. and contributors");
});

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
	Accounting: "Chart of accounts, invoicing, payments and financial reports.",
	Assets: "Track and depreciate company assets.",
	Buying: "Purchase orders, suppliers and procurement.",
	CRM: "Leads, deals and customer relationships.",
	HRMS: "Employees, leave, payroll and attendance.",
	Projects: "Tasks, timesheets and project tracking.",
	Selling: "Quotations, sales orders and customers.",
	Stock: "Inventory, warehouses and stock movement.",
};

const PT_DESKTOP_ICON_IMAGES = Object.fromEntries(
	Object.keys(PT_DESKTOP_ICON_DESCRIPTIONS).map((label) => [
		label,
		// `/assets/promit10sui/images/desktop/${label}.jpeg`,
		`/assets/promit10sui/images/prommittensicon.png`,
	])
);
const PT_DESKTOP_ICON_LABELS = {
	"Promittens CRM": "CRM",
	"Promittens HR": "HRMS",
	"Frappe HR": "HRMS",
};

function pt_customize_desktop_icons() {
	document.querySelectorAll(".desktop-container .desktop-icon").forEach((icon) => {
		const title = icon.querySelector(".icon-title");
		const label = [icon.getAttribute("data-id"), title?.textContent]
			.map((value) => value?.trim())
			.map((value) => PT_DESKTOP_ICON_LABELS[value] || value)
			.find((value) => Object.hasOwn(PT_DESKTOP_ICON_IMAGES, value));
		// Branding must never remove modules supplied by the site's desktop settings.
		if (!label) return;
		if (title) {
			title.textContent = label;
			title.setAttribute("data-original-title", label);
		}

		let container = icon.querySelector(":scope > .icon-container");
		if (!container) {
			container = document.createElement("div");
			container.className = "icon-container";
			icon.prepend(container);
		}
		container.className = "icon-container";
		container.replaceChildren();

		const image = document.createElement("img");
		image.className = "app-icon";
		image.src = PT_DESKTOP_ICON_IMAGES[label];
		image.alt = label;
		container.appendChild(image);
	});
}

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
	$(".desktop-navbar .navbar-home #brand-logo").attr({
		src: "/assets/promit10sui/images/prommittensicon.png",
		alt: "Prommittens Technologies",
	});
	// desktop.js finishes wiring up the grid synchronously before this fires,
	// but tooltips/labels are set in the same tick — a micro-delay avoids a
	// race where our div gets read before class names settle.
	setTimeout(() => {
		pt_customize_desktop_icons();
		pt_add_desktop_icon_descriptions();
	}, 0);
});

// Also handle desktops rendered before this script loads, and menus created
// by versions of Frappe that do not use the desktop_screen event.
$(function () {
	function customize_rendered_desktop() {
		pt_customize_desktop_icons();
		pt_add_desktop_icon_descriptions();
	}
	function remove_support_menu_item() {
		document.querySelectorAll(".frappe-menu .menu-item-title").forEach((title) => {
			if (title.textContent.trim() === __("Frappe Support")) {
				title.closest(".dropdown-menu-item")?.remove();
			}
		});
	}
	customize_rendered_desktop();
	remove_support_menu_item();
	const observer = new MutationObserver((records) => {
		let desktop_added = false;
		let menu_added = false;
		for (const record of records) {
			for (const node of record.addedNodes) {
				if (node.nodeType !== 1) continue;
				desktop_added ||= node.matches(".desktop-icon") || !!node.querySelector(".desktop-icon");
				menu_added ||= node.matches(".frappe-menu, .menu-item-title") ||
					!!node.querySelector(".menu-item-title");
			}
		}
		if (desktop_added) customize_rendered_desktop();
		if (menu_added) remove_support_menu_item();
	});
	observer.observe(document.body, { childList: true, subtree: true });
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
