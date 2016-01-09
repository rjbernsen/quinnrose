function toggleChevron(e) {
	$(e.target).prev('.widget-header').find("span.fa").toggleClass(
			'fa-chevron-down fa-chevron-up');
}

var editorOptions = {
	'texteffects' : true,
	'aligneffects' : true,
	'textformats' : true,
	'fonteffects' : true,
	'actions' : true,
	'insertoptions' : true,
	'extraeffects' : true,
	'advancedoptions' : true,
	'screeneffects' : true,
	'bold' : true,
	'italics' : true,
	'underline' : true,
	'ol' : true,
	'ul' : true,
	'undo' : true,
	'redo' : true,
	'l_align' : true,
	'r_align' : true,
	'c_align' : true,
	'justify' : true,
	'insert_link' : true,
	'unlink' : true,
	'insert_img' : false,
	'hr_line' : true,
	'block_quote' : true,
	'source' : true,
	'strikeout' : true,
	'indent' : true,
	'outdent' : true,
//	'fonts' : fonts,
//	'styles' : styles,
	'print' : false,
	'rm_format' : true,
	'status_bar' : true,
//	'font_size' : fontsizes,
//	'color' : colors,
//	'splchars' : specialchars,
	'insert_table' : true,
	'select_all' : true,
	'togglescreen' : false
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

//	$("#id_lead_text").Editor(editorOptions);
	$("#id_article_text").Editor(editorOptions);

	$('#new_post_form').submit(function() {
		try {
//			alert($('.Editor-editor').html());
			$('#id_article_text').text($('.Editor-editor').html());
//			alert($('#id_article_text').text());
		} catch(err) {
			alert(err.message);
			return false;
		}
	});

	try {
//		alert($('.Editor-editor').html());
		$('.Editor-editor').html($('#id_article_text').text());
//		alert($('#id_article_text').text());
	} catch(err) {
		alert(err.message);
		return false;
	}
});

