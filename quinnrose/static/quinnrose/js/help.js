function setCategoryLabel() {
	var label = $("#" + cur_category + "_category").text();
	$("#help-category-menu").html(label + ' <span class="caret"></span>');
	$("#help-category-menu").css({
		'visibility' : 'visible'
	});
}

$(document).ready(function() {
	setCategoryLabel();
});
