const formOutput = document.querySelector('.form-output-container');

document.querySelector('#main-form').addEventListener('submit', e => {
	e.preventDefault();

	//get form data
	const data = new FormData(e.target);
	const formData = Object.fromEntries(data.entries());
	handleCharFormSubmission(formData);
});

function handleCharFormSubmission(data) {
	clearFormOutput();

	//from form data passed in, need to pull out text and character to search for in text
	const text = data['search-text'];
	const searchChar = data['search-character'];

	let count = getOccurrencesOfChar(text, searchChar);

	displayResult(count, searchChar);
}

function getOccurrencesOfChar(text, searchChar) {
	//given a string and a single character, check how many times character occurs in the string

	const splitString = text.replace(/ /g, '').split('');

	return splitString.reduce(function (total, value) {
		return value.toLowerCase() === searchChar.toLowerCase() ? total + 1 : total;
	}, 0);
}

function displayResult(count, searchChar) {
	//takes in a number representing occurences of user-input char in user-input text, and updates the DOM accordingly

	if (count === 0) {
		let zeroResultWindow = window.open('', '', 'width=300,height=100');
		zeroResultWindow.document.body.innerText = `No occurences were found of ${searchChar}`;
	} else {
		formOutput.innerText = `${count} occurrences were found within the text provided`;
	}
}

function clearFormOutput() {
	formOutput.innerHTML = '';
}
