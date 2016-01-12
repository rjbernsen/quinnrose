var homeSearchForm;

function goSearch(subType) {

	var action = homeSearchForm.attr('action') + '/' + subType;

	homeSearchForm.attr('action', action);
	homeSearchForm.submit();
}

$(document).ready(function(e) {

	homeSearchForm = $('#home_search_form');
	
//	homeSearchForm.submit(function() {
//
//	});

	$('#search_submit_button').click(function() {
		goSearch('general');
	});
});

