DEFAULT_ALERT_CLOSE_DELAY = 5000;
DEFAULT_ALERT_TYPE = "info";

/*
All jQuery AJAX posts require this! 
*/
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/*
---------------------------------------------------------
Popovers
---------------------------------------------------------
 */
var isIOS;
var isAndroid;

$(function () {
})

function checkPopovers() {
	if ($(window).width() <= 992) {
		$('[data-toggle="popover"]').popover('hide').popover('disable');
	}
	else
	{
		$('[data-toggle="popover"]').popover('enable');
	}
}
$(document).ready(function(){

	isIOS = /iPad|iPhone|iPod/.test(navigator.platform);
	isAndroid = /(android)/i.test(navigator.userAgent);

	checkPopovers();
	
	$(window).resize(function() {
		checkPopovers();
	});
});

/*
Temporary non-modal alerts 
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
        $("body")
            .append( $('<div id="alerts-container" class="alert-popup-fade">') );
    }

    // create the alert div
    var alert_html = $('<div class="alert alert-' + type + ' fade in">')
        .append(
            $('<button type="button" class="close" data-dismiss="alert">')
            .append("&times;")
        )
        .append(message);

    // add the alert div to top of alerts-container, use append() to add to bottom
    $("#alerts-container").prepend(alert_html);

    // if closeDelay was passed - set a timeout to close the alert
    if (closeDelay)
        window.setTimeout(function() { alert_html.alert("close") }, closeDelay);     
}

