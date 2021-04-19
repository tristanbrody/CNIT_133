// Part 1:
// Create a webpage containing a form that displays an input text box, a group of radio buttons, a group of checkboxes, and select items (a drop-down or datalist element); along with a script that executes form validation.

// Your script should validate whether the user has entered data in the input text box, has checked a radio button, has checked at least one checkbox, and has selected an option from the list of options in the select (or datalist) element.

// Use a submit button to invoke the validation script, so that the form is processed only when the form fields are ALL valid. If a field is invalid then display a message to the user.

// In your form statement, use method="post" and an action that can be a mailto or a webpage(displaying that the form has been processed), but be sure to use input type="submit" for your submit button. Alternatively you can leave out the form's action and method, but then you should use an input type="button", along with displaying any appropriate messages.

// Make sure that if you display an error message because of a single field, you do not clear out the whole entire form unless all the fields would have error messages associated to them! It's horrible to have the user fill out all the form again when there was only one field with error, right? Remember about this type of detail that is related to user experience!

window.addEventListener('DOMContentLoaded', () => {
	const myForm = document.querySelector('#main-form');
	//use Array.from to convert node listing we get back from querySelectorAll into a standard array
	const formElements = Array.from(document.querySelectorAll('.container input'));
	const checkboxes = Array.from(document.querySelectorAll('#main-form input[type="checkbox"]'));

	myForm.addEventListener('submit', e => {
		e.preventDefault();
		//clear out values from previous submission of form
		const invalidElements = [];
		clearOutExistingErrorMessages(document.querySelectorAll('.error-message'));

		//for the text inputs, we can use checkValidity to check the user-entered data
		for (element of formElements) {
			if (['text', 'datalist'].includes(element.type)) {
				//for datalist, we'll call a helper function to make sure value selected is part of the datalist
				if (element.list != ('' || undefined)) {
					if (!getAllowedDatalistValues(element.id).includes(element.value)) {
						invalidElements.push({ id: element.id, type: 'datalist' });
						break;
					}
				}
				if (!element.checkValidity()) invalidElements.push({ id: element.id, type: element.type });
			}
		}
		//radio button has first option pre-selected, so cannot be invalid

		validCheckboxes = validateCheckboxGroup(checkboxes);

		if (!validCheckboxes) invalidElements.push({ id: 'checkbox-container', type: 'checkbox' });

		//if all other elements are valid and at least one checkbox is selected, reload the page
		validInput = invalidElements.length === 0;

		//ordinarily would send this data to our server to pass to database, but for this example will just reload the page to clear inputs
		if (validInput) {
			window.location.reload();
		}
		// input is not valid, so we'll pass array of invalidElements to errorMessageController
		errorMessageController(invalidElements);
	});
});

function validateCheckboxGroup(checkboxes) {
	//make sure at least one checkbox is checked out of a group
	return checkboxes.some(checkbox => checkbox.checked);
}

function getErrorMessage(type) {
	//get error message based on element type
	return errorMessages[type];
}

function errorMessageController(invalidElements) {
	/* handle adding error messages to DOM, when given an array of invalid elements. Array is an array of objects. Each object contains id of 
    invalid input element and input type */
	for (invalidElement of invalidElements) {
		let { id, type } = invalidElement;
		let div = document.createElement('div');
		let errorMessage = getErrorMessage(type);
		document.querySelector(`#${id}-error`).innerText = errorMessage;
	}
}

function clearOutExistingErrorMessages(errorMessages) {
	//clear out error messages from previous submission of form
	for (errorMessage of errorMessages) {
		errorMessage.innerText = '';
	}
}

function getAllowedDatalistValues(id) {
	//given an id for a datalist, return the values for each corresponding option
	datalist = Array.from(document.querySelectorAll(`#${id}-set option`));
	const values = [];
	for (option of datalist) {
		console.log(option);
		values.push(option.value);
	}
	return values;
}

const errorMessages = {
	checkbox: 'Please select at least one option',
	radio: '',
	text: 'Please provide a response',
	datalist: 'Your selection must be from the dropdown menu'
};
