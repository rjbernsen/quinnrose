var options = {
  enableHighAccuracy: true,
  timeout: 10000,
  maximumAge: 0
};
function success(position) {
	lat = position.coords.latitude;
	lon = position.coords.longitude;
	var msg = "Latitude: " + lat + "<br>Longitude: " + lon;
//	showAlert(msg, 5000);

	if (locationChanged(lat, lon)) {
	
	//	$.cookie('current_lat',position.coords.latitude);
		var data_request = {
			current_lat: lat,
			current_lon: lon
		};
		$.post('/session_post', 
			data_request,
			function(data_response) {
				if (data_response == 'ok') {
					showAlert(msg);
				}
			}
		);
	}
	
}
function error(err) {
	var msg = 'ERROR(' + err.code + '): ' + err.message;
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
This function is only for checking to see if the zip code
(general location) has changed.
*/
function locationChanged(lat, lon) {
	var old_lat = parseFloat(current_coords.lat).toFixed(3);
	var old_lon = parseFloat(current_coords.lon).toFixed(3);
	var new_lat = parseFloat(lat).toFixed(3);
	var new_lon = parseFloat(lon).toFixed(3);
	
//	var msg = 'old_lat=' + old_lat + '<br>new_lat=' + new_lat + '<br>old_lon=' + old_lon + '<br>new_lon=' + new_lon;
//	showAlert(msg);
	return new_lat != old_lat || new_lon != old_lon;
}

getLocation();

//showAlert($.session.get('current_lat'));
