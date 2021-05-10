const formOutput = document.querySelector('.form-output-container');

//declare some regex we can use throughout the script
const fullReMatch = /^(\(?\d{3}[-\.\)]?)(\d{3}[-\.\)]?)(\d{4})$/;

document.querySelector('input#phone-input').addEventListener('keyup', e => {
	checkPhoneInput(e.target);
});

function checkPhoneInput(input) {
	const numberAsString = input.value.toString();
	const checkForMatch = numberAsString.match(fullReMatch);

	if (input.value.replace(/\D/g, '').length > 10) {
		addErrorMessageToDom();
	}

	//if there is a regex match, we can clear any previous results, and add a line to the DOM for each group in the phone number
	if (checkForMatch) {
		clearFormOutput();
		addFullEntryToDom(input.value);
		addAreaCodeToDom(checkForMatch[1].replace(/[\D\.\-\)]/g, ''));
		addMiddleDigitsToDom(checkForMatch[2].slice(0, 3));
		addLastDigitsToDom(checkForMatch[3].slice(0, 5));
		input.value = '';
	}
	//fires via event listener every time a key is entered in phone input on form
}

function addFullEntryToDom(input) {
	formOutput.innerHTML += `
        <p></em>Your entry: </em>${input}</p>
    `;
}

function addAreaCodeToDom(areaCode) {
	formOutput.innerHTML += `
        <p><em>Area code: </em>${areaCode}</p>
    `;
}

function addMiddleDigitsToDom(middleDigits) {
	formOutput.innerHTML += `
        <p><em>Middle three digits: </em>${middleDigits}</p>
    `;
}

function addLastDigitsToDom(lastDigits) {
	formOutput.innerHTML += `
        <p><em>Last three digits: </em>${lastDigits}</p>
    `;
}

function clearFormOutput() {
	formOutput.innerHTML = '';
}

function addErrorMessageToDom() {
	formOutput.innerHTML = 'Error: Phone number cannot exceed 10 digits';
}
