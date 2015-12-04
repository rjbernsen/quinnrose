


$('select').change(function() {
 if ($(this).children('option:first-child').is(':selected')) {
   $(this).addClass('select-placeholder');
 } else {
  $(this).removeClass('select-placeholder');
 }
});





// ----------------------------------------------
// Sign in form
//----------------------------------------------
//$(function() {
//
//    $('#signin-form-link').click(function(e) {
//		$("#signin-form").delay(100).fadeIn(100);
// 		$("#register-form").fadeOut(100);
//		$('#register-form-link').removeClass('active');
//		$(this).addClass('active');
//		e.preventDefault();
//	});
//	$('#register-form-link').click(function(e) {
//		$("#register-form").delay(100).fadeIn(100);
// 		$("#signin-form").fadeOut(100);
//		$('#signin-form-link').removeClass('active');
//		$(this).addClass('active');
//		e.preventDefault();
//	});
//
//});
//
//
