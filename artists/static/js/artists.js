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

var headshotContainerJQ;
var headshotHeaderJQ;
var frameCanvasJQ;
var headshotCanvasJQ;
var frameEdgeSize = 64;
var preferredWidth = 300;

$('#headshot').click(function(){
	
	$('#headshot-background').css({
		visibility: 'visible'
	});
	
	if (!headshotContainerJQ) {
		headshotContainerJQ = $('#headshot-container');
	    headshotHeaderJQ = $('#headshot-header');
	    frameCanvasJQ = $('#headshot-frame-canvas');
	    headshotCanvasJQ = $('#headshot-photo-canvas');
		
	    var headshotHeader = document.getElementById('headshot-header');
		var frameCanvas = document.getElementById('headshot-frame-canvas');
		var headshotCanvas = document.getElementById('headshot-photo-canvas');
		var frameImage = document.getElementById('headshot-frame-img');
		var headshotImage = document.getElementById('headshot-photo-img');
		
		var frameWidth = frameImage.width;
		var frameHeight = frameImage.height;
		var headshotWidth = headshotImage.width;
		var headshotHeight = headshotImage.height;
		
		// Get new dimensions for the headshot.
		var newHeadshotWidth = preferredWidth;
		var newHeadshotHeight = (newHeadshotWidth / headshotWidth) * headshotHeight;
		
		// Get the height and width of the frame top (and bottom)
		// and left (and right) from a resized version of the frame.
		var newFrameLeftSize = (frameEdgeSize * newHeadshotWidth / frameWidth) - 1;
		var newFrameTopSize = (frameEdgeSize * newHeadshotHeight / frameHeight) - 1;
		var newFrameWidth = newHeadshotWidth + (newFrameLeftSize * 2);
		var newFrameHeight = newHeadshotHeight + (newFrameTopSize * 2);
		
		headshotHeader.width = newFrameWidth;
		frameCanvas.width = newFrameWidth;
		frameCanvas.height = newFrameHeight;
		headshotCanvas.width = newFrameWidth;
		headshotCanvas.height = newFrameHeight;
		
		frameImage.width = newFrameWidth;
		frameImage.height = newFrameHeight;
	
	    frameCanvas.getContext("2d")
	    .drawImage(
			frameImage,
			0,
			0,
			frameWidth,
			frameHeight,
			0,
			0,
			newFrameWidth,
			newFrameHeight
	    );
	
	    headshotCanvas.getContext("2d")
	    .drawImage(
			headshotImage,
			0,
			0,
			headshotWidth,
			headshotHeight,
			newFrameLeftSize,
			newFrameTopSize,
			newHeadshotWidth,
			newHeadshotHeight
	    );
		
	    headshotHeaderJQ.css({
	    	top: 80,
	    	width: newFrameWidth
	    });
		frameCanvasJQ.css({
	    	top: 100
	    });
		headshotCanvasJQ.css({
	    	top: 100
	    });
	    headshotContainerJQ.css({
	    	width: newFrameWidth
	    });
	}
	
    headshotHeaderJQ.css({
    	visibility: 'visible'
    });
	frameCanvasJQ.css({
    	visibility: 'visible'
    });
	headshotCanvasJQ.css({
    	visibility: 'visible'
    });
	
	setHeadshotPosition();
	
	return;

});

$('#headshot-close').click(function(){
	$('#headshot-background').css({
		visibility: 'hidden'
	});
	
    headshotHeaderJQ.css({
    	visibility: 'hidden'
    });
    frameCanvasJQ.css({
    	visibility: 'hidden'
    });
    headshotCanvasJQ.css({
    	visibility: 'hidden'
    });
});



function setHeadshotPosition() {
    var width = $(window).width();
    var containerWidth = $('#headshot-container').width();  
    var leftMargin = (width - containerWidth) / 2;    
    $('#headshot-container').css('left', leftMargin);    
}

$(document).ready(function() {
//    setHeadshotPosition();
    $(window).resize(function() {
    	setHeadshotPosition();    
    });
});

