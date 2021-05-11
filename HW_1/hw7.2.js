$(document).ready(function () {
	$('.hoverable-div').hover(
		function () {
			$('.hoverable-nav-links').show();
		},
		function () {
			$('.hoverable-nav-links').hide();
		}
	);
});
