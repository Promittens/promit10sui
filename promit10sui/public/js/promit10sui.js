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
