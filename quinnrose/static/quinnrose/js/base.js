var DEBUG = false;

var DEFAULT_ALERT_CLOSE_DELAY = 5000;
var DEFAULT_ALERT_TYPE = "info";

/*
 * All jQuery AJAX posts require this!
 */
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
	beforeSend : function(xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});

/*
---------------------------------------------------------
Menu search form
---------------------------------------------------------
*/
var menuSearchForm;

function goMenuSearch() {

	var subType = $('input:radio[name=search_what]:checked').val();
	var action = menuSearchForm.attr('action') + '/' + subType;
	menuSearchForm.attr('action', action);
}

$(document).ready(function(e) {

	menuSearchForm = $('#search_form');
	
	menuSearchForm.submit(function() {
		goMenuSearch()
	});
});


/*
---------------------------------------------------------
Popovers
---------------------------------------------------------
*/
var isIOS;
var isAndroid;

function checkPopovers() {
	if ($(window).width() <= 992) {
		$('[data-toggle="popover"]').popover('hide').popover('disable');
	} else {
		$('[data-toggle="popover"]').popover('enable');
	}
}

function showSpinner() {
	spinner.css({
		visibility : 'visible'
	});
}
function hideSpinner() {
	spinner.css({
		visibility : 'hidden'
	});
}

var spinner = $('#spinner');

$(document).ready(function() {

	if (DEBUG) { 
		$(window).resize(function() {
			showAlert($(window).width() + ' x ' + $(window).height(), 2000);
		});
	}
	
	isIOS = /iPad|iPhone|iPod/.test(navigator.platform);
	isAndroid = /(android)/i.test(navigator.userAgent);

	checkPopovers();

	$(window).resize(function() {
		checkPopovers();
	});

	spinner.position({
		my : 'center top+120',
		at : 'center top+120',
		of : 'body'
	});

});

/*
 * Temporary non-modal alerts
 */
function showAlert(message, closeDelay, type) {

	if (closeDelay === undefined) {
		closeDelay = DEFAULT_ALERT_CLOSE_DELAY;
	}
	if (type === undefined) {
		type = DEFAULT_ALERT_TYPE;
	}

	if ($("#alerts-container").length == 0) {
		// alerts-container does not exist, add it
		$("body").append(
				$('<div id="alerts-container" class="alert-popup-fade">'));
	}

	// create the alert div
	var alert_html = $('<div class="alert alert-' + type + ' fade in">')
			.append(
					$(
							'<button type="button" class="close" data-dismiss="alert">')
							.append("&times;")).append(message);

	// add the alert div to top of alerts-container, use append() to add to
	// bottom
	$("#alerts-container").prepend(alert_html);

	// if closeDelay was passed - set a timeout to close the alert
	if (closeDelay)
		window.setTimeout(function() {
			alert_html.alert("close")
		}, closeDelay);
}
