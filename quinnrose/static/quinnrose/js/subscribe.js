function setCategoryLabel() {
	var levelObj = $('#id_level');
	levelObj.val(level);
	levelObj.removeClass('select-placeholder');
}

var savedPlanDivHtml;
var savedPlanSavingsHtml;

function updateFrequencyPanel() {
	var levelObj = $('#id_level');
	var freqObj = $('#id_billing_frequency');
	var level = levelObj.val();
	var freq = freqObj.val();
	var levelLabel = $('#id_level option[value="' + level + '"]').text();
	var info_id = level + '_' + freq;
	var cur_info = billing_info[info_id];
	// alert(info_id);

	if (info_id.length < 3) {
		$('#plan-div').html('Select a level and a billing frequency...');
	} else {
		$('#plan-div').html(savedPlanDivHtml);
		$('#plan-level').html(levelLabel);
		$('#plan-price').html(cur_info['price']);

		if (cur_info['price'] == 'Free') {
			$('#plan-label').html('');
		} else {
			$('#plan-label').html(cur_info['label']);
		}
		if (cur_info['label'] == 'yearly' && cur_info['savings'] != 'None') {
			$('#plan-savings-text').html(savedPlanSavingsHtml);
			$('#plan-savings').html(cur_info['savings']);
		} else {
			$('#plan-savings-text').html('');
		}
	}
}

$(document).ready(function() {

	savedPlanDivHtml = $('#plan-div').html();
	savedPlanSavingsHtml = $('#plan-savings-text').html();

	$('#id_billing_frequency').val('1');
	setCategoryLabel();
	updateFrequencyPanel();

	$('#id_level').change(function() {
		updateFrequencyPanel();
	});
	$('#id_billing_frequency').change(function() {
		updateFrequencyPanel();
	});
});
