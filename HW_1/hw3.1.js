//declare DOM elements
let studentName = document.querySelector('#student-name').value;
let studentNameInput = document.querySelector('#student-name');
const form = document.querySelector('#input-form');
const inputDiv = document.querySelector('#input-div');

//declare variables for grade inputs
let inputNodeList = document.querySelectorAll('.grade-value');
const inputArray = Array.from(inputNodeList);
let finalValues = {};

//run function to store original value of placeholders on grade inputs in object
let placeHolderValues = getOriginalPlaceholders();
//event listener to update placeholder values for grade inputs based on user entering the student's name
studentNameInput.addEventListener('blur', e => {
	updateStudentName(e.target.value);
	updatePlaceHolderForGradeInputs(e.target.value);
	if (studentName.match(/[0-9]?.*[0-9]/)) {
		studentNameInput.style.boxShadow = '0 0 3px #CC0000';
	}
	// box-shadow: 0 0 3px #CC0000
});

form.addEventListener('submit', e => {
	inputDiv.innerHTML = '';
	e.preventDefault();
	if (validateInput(getValuesFromInputs())) {
		calculateFinalAverage();
	}
});

//functions for event listeners

function updateStudentName(name) {
	studentName = name;
}

function updatePlaceHolderForGradeInputs(name) {
	for (let input of inputArray) {
		let inputType = input.type;
		let placeholderValue = placeHolderValues[inputType]['placeholder'];
		if (name === '') {
			input.setAttribute('placeholder', placeholderValue);
		} else {
			input.setAttribute('placeholder', `${placeholderValue} for ${name}`);
		}
	}
}

function getOriginalPlaceholders() {
	let placeholderObj = {};
	for (let input of inputArray) {
		let inputType = input.type;
		let placeholderValue = input.getAttribute('placeholder');
		placeholderObj[inputType] = { placeholder: placeholderValue };
	}
	return placeholderObj;
}

function getValuesFromInputs() {
	let inputValues = [];
	for (let input of inputArray) {
		let inputType = input.type;
		inputValues.push({
			type: inputType,
			id: input.id,
			value: input.value,
			name: input.getAttribute('data-name')
		});
	}
	return inputValues;
}

function validateInput(inputValues) {
	let validInput = true;
	if (!validName(studentName)) {
		let linebreak = document.createElement('br');
		inputDiv.append(`Please correct your input for student name`, linebreak);
		validInput = false;
	} else {
		finalValues['name'] = studentName;
	}
	for (let val of inputValues) {
		if (val['type'] === 'number') {
			if (!onlyNums(val['value']) || val['value'] > 100 || containsZero(val['value'])) {
				let linebreak = document.createElement('br');
				inputDiv.append(`Please correct your input for ${val['name']}`, linebreak);
				validInput = false;
			} else {
				finalValues[val['id']] = val['value'];
			}
		}
	}
	return validInput;
}

function calculateFinalAverage() {
	let hwAvg = finalValues['homework-average'];
	let midtermGrade = finalValues['mid-term-exam-score'];
	let finalExamScore = finalValues['final-exam-score'];
	let participation = finalValues['participation'];
	let finalAverage = Math.round(0.5 * hwAvg + 0.2 * midtermGrade + 0.2 * finalExamScore + 0.1 * participation);
	inputDiv.append(`${studentName}'s final average for the course is ${finalAverage}`);
}
