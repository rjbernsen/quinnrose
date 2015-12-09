

var starElemGold = document.getElementById('goldstar');
var starElemGray = document.getElementById('graystar');
var ratingElems = document.getElementsByName('rating');

for (var i = 0; i < ratingElems.length; i++) {
	var elem = ratingElems[i];
	var starCount = elem.dataset.starCount;
	var rating = elem.dataset.rating;
	
	for (var j = 0; j < starCount; j++) {
		var node;

		if (j < rating) {
			node = starElemGold.cloneNode();
		}
		else {
			node = starElemGray.cloneNode();
		}
		node.className += '-show';
		elem.appendChild(node);
	}
}