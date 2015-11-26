


$('select').change(function() {
 if ($(this).children('option:first-child').is(':selected')) {
   $(this).addClass('select-placeholder');
 } else {
  $(this).removeClass('select-placeholder');
 }
});