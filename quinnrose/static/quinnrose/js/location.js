var options = {
	enableHighAccuracy : true,
	timeout : 15000,
	maximumAge : 0
};
function get_message(lat, lon) {
	return "Latitude: " + lat + "<br>Longitude: " + lon;
}
function success(position) {
	lat = position.coords.latitude;
	lon = position.coords.longitude;
	var msg = get_message(lat, lon);
	// showAlert(msg, 5000);

	if (locationChanged(lat, lon)) {

		// $.cookie('current_lat',position.coords.latitude);
		var data_request = {
			current_lat : lat,
			current_lon : lon
		};
		$.post('/session_post', data_request, function(data_response) {
			if (data_response == 'ok') {
				data_request['command'] = 'get_postal_code';

				$.get('/geonames', data_request, function(data_response) {
					if (data_response) {
						msg += '<br>Postal Code: ' + data_response;
						showAlert(msg);
					}
				});
			}
		});

	}

}
function error(err) {
	// var msg = 'ERROR(' + err.code + '): ' + err.message;
	var lat_lon_msg = get_message(current_coords['lat'], current_coords['lon']);
	var msg = 'Could not connect to the location service. Using previous location:<br>'
			+ lat_lon_msg;
	showAlert(msg, 10000, 'danger');
}

function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(success, error, options);
	} else {
		showAlert("Your browser doesn't support capturing your location!", 4000);
	}
}

/*
 * This function is only for checking to see if the zip code (general location)
 * has changed.
 */
function locationChanged(lat, lon) {
	var old_lat = parseFloat(current_coords.lat).toFixed(3);
	var old_lon = parseFloat(current_coords.lon).toFixed(3);
	var new_lat = parseFloat(lat).toFixed(3);
	var new_lon = parseFloat(lon).toFixed(3);

	// var msg = 'old_lat=' + old_lat + '<br>new_lat=' + new_lat +
	// '<br>old_lon=' + old_lon + '<br>new_lon=' + new_lon;
	// showAlert(msg);
	return new_lat != old_lat || new_lon != old_lon;
}

$(document).ready(function(e) {

	getLocation();

});
