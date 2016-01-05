/*
-------------------------------------------------------------------
Skill stars
-------------------------------------------------------------------
*/
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

/*
-------------------------------------------------------------------
Headshots
-------------------------------------------------------------------
*/
var headshotContainerJQ;
var headshotHeaderJQ;
var frameCanvasJQ;
var headshotCanvasJQ;
var popupTop = 100;
var headerHeight = 40;
var headerWidth = 40;
var frameEdgeSize = 64;
var preferredWidth = 300;

$('#headshot').click(function(){

	var windowWidth = $(window).width();

	// Check the size for smaller screens.
	if (windowWidth < preferredWidth + (frameEdgeSize * 2)) {
		preferredWidth = windowWidth - (frameEdgeSize * 2);
	}
	
	$('#headshot-background').css({
		visibility: 'visible'
	});
	
	headshotContainerJQ = $('#headshot-container');
    headshotHeaderJQ = $('#headshot-header');
    frameCanvasJQ = $('#headshot-frame-canvas');
    headshotCanvasJQ = $('#headshot-photo-canvas');
	
    var headshotHeader = document.getElementById('headshot-header');
	var frameCanvas = document.getElementById('headshot-frame-canvas');
	var headshotCanvas = document.getElementById('headshot-photo-canvas');
	var frameImage = document.getElementById('headshot-frame-img').cloneNode();
	var headshotImage = document.getElementById('headshot-photo-img').cloneNode();
	
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
	var headerLeftPos = (newFrameWidth - headerWidth);
	
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
    	top: popupTop,
    	left: headerLeftPos
    });
	frameCanvasJQ.css({
    	top: popupTop + headerHeight
    });
	headshotCanvasJQ.css({
    	top: popupTop + headerHeight
    });
    headshotContainerJQ.css({
    	width: newFrameWidth
    });
	
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

$('#headshot-header').click(function(){
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
    $(window).resize(function() {
    	setHeadshotPosition();    
    });
});

