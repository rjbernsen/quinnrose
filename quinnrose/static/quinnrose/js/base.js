var isIOS;
var isAndroid;

/*
---------------------------------------------------------
Popovers
---------------------------------------------------------
 */
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

