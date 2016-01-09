function toggleChevron(e) {
    $(e.target)
        .prev('.widget-header')
        .find("span.fa")
        .toggleClass('fa-chevron-down fa-chevron-up');
}

$(document).ready(function() {

	$('#latest_posts').on('hidden.bs.collapse', toggleChevron);
	$('#latest_posts').on('shown.bs.collapse', toggleChevron);
	$('#categories').on('hidden.bs.collapse', toggleChevron);
	$('#categories').on('shown.bs.collapse', toggleChevron);
	$('#recent_comments').on('hidden.bs.collapse', toggleChevron);
	$('#recent_comments').on('shown.bs.collapse', toggleChevron);
	$('#tags').on('hidden.bs.collapse', toggleChevron);
	$('#tags').on('shown.bs.collapse', toggleChevron);

});
