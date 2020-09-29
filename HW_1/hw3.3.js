let outputDiv = document.querySelector('#output-div');
let input = document.querySelector("[data-type='main-input']");
let output = document.querySelector("[data-type='main-output']");
let allButtons = Array.from(document.querySelectorAll('button'));

for (let btn of allButtons) {
	btn.addEventListener('click', e => {
		e.preventDefault();
		outputDiv.innerText = '';
		if (!onlyNumsNegativeAllowed(input.value)) {
			invalidInput();
		} else if (e.target.dataset.type === 'to-celsius') {
			let celsiusVal = toCelsius(input.value);
			outputDiv.append(`${Math.round(input.value)} degrees Farenheit is ${celsiusVal} degrees Celsius`);
		} else if (e.target.dataset.type === 'to-faren') {
			let farensVal = toFarens(input.value);
			outputDiv.append(`${Math.round(input.value)} degrees Celsius is ${farensVal} degrees Farenheit`);
		}
	});
}

function invalidInput() {
	outputDiv.append('Please correct your input');
}

function toCelsius(input) {
	return Math.round((5 / 9) * (input - 32));
}

function toFarens(input) {
	return Math.round((9 / 5) * input + 32);
}
