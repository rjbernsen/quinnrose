
$(function() {
	$(document).on("click", "a.fileDownload", function() {

		$.fileDownload($(this).attr('href'), {
			preparingMessageHtml: "Your download is be prepared, please wait...",
			failMessageHtml: "There was a problem generating your download, please try again."
		});
		
		return false; //this is critical to stop the click event which will trigger a normal file download!
	});
});
 