const formOutput = document.querySelector('.form-output-container');

document.querySelector('#main-form').addEventListener('submit', e => {
	e.preventDefault();

	//get form data
	const data = new FormData(e.target);
	const formData = Object.fromEntries(data.entries());
	handleFormSubmission(formData);
});

function handleFormSubmission(data) {
	clearFormOutput();

	//check if number has at least 4 decimal places
	let re = /\d+\.\d{4}\d*/;
	let num = data['number-entry'];

	let numAsString = num.toString();

	if (!re.test(numAsString)) {
		formOutput.append('Invalid input - number must have at least 4 decimal places');
		return;
	}

	//number passed regex check - call functions to append exciting data about the number

	addFormOutput([
		getOriginalIntegerText(num),
		getNearestIntegerText(num),
		getRoundedSquareRootText(num),
		getNearestTenthsPositionText(num),
		getNearestHundredthsPositionText(num),
		getNearestThousandthsPositionText(num)
	]);
}

function clearFormOutput() {
	formOutput.innerHTML = '';
}

function addFormOutput(arrayData) {
	let ul = document.createElement('ul');
	for (let entry of arrayData) {
		let li = document.createElement('li');
		li.innerText = entry;
		ul.append(li);
	}
	formOutput.append(ul);
}

function getOriginalIntegerText(num) {
	return `Number entered: ${num}`;
}

function getNearestIntegerText(num) {
	return `Rounded to nearest integer: ${Math.round(num)}`;
}

function getRoundedSquareRootText(num) {
	return `Square route rounded to nearest integer: ${Math.round(Math.sqrt(num))}`;
}

function getNearestTenthsPositionText(num) {
	return `Rounded to nearest tenths position: ${Math.round(10 * num) / 10}`;
}
function getNearestHundredthsPositionText(num) {
	return `Rounded to nearest hundredths position: ${Math.round(100 * num) / 100}`;
}
function getNearestThousandthsPositionText(num) {
	return `Rounded to nearest thousandths position: ${Math.round(1000 * num) / 1000}`;
}
