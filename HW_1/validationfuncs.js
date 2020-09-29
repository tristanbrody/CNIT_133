//functions shared across this project for validating inputs

//checks that name isn't blank and doesn't contain numbers
function validName(name) {
	let regex = /[0-9]?.*[0-9]/;
	return name !== '' && !regex.test(name.toString());
}

//checks that input is only a number (zero or higher)
function onlyNums(input) {
	let regex = /^[0-9]+$/;
	return regex.test(input.toString());
}

function onlyNumsNegativeAllowed(input) {
	let regex = /^[-0-9]+$/;
	return regex.test(input.toString());
}

//checks for zero
function containsZero(input) {
	let regex = /^00?/;
	return regex.test(input.toString());
}
