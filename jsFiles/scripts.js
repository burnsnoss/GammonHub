var hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'];

function generateColor() {

	var hexColor = '#';
	var x = 0;

	for (var i = 0; i < 6; i++) {
		x = Math.round(Math.random() * 15);
		hexColor = hexColor + hexValues[x];
	};

	return hexColor;
};

// var i = 0;

setInterval(function() {
	// if (i % 2 == 0) {
	// 	$('#page').css('backgroundColor', '#FFFFFF');
	// }	else {
	// 	$('#page').css('backgroundColor', generateColor());
	// };
	// i = i + 1;

	$('#page').css('backgroundColor', generateColor());

}, 200);
