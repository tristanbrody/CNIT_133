//declare DOM elements
$(document).ready(function () {
	const studentGrades = JSON.parse(localStorage.getItem('studentGrades') || '[]');
	let studentName = document.querySelector('#student-name').value;
	let studentNameInput = document.querySelector('#student-name');
	const form = document.querySelector('#input-form');
	const inputDiv = document.querySelector('#input-div');
	const template = document.getElementById('student-grades-template');
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

	document.getElementById('enter-new-grade').addEventListener('click', e => {
		e.preventDefault();
		$('#main-inputs-div').slideToggle();
		document.getElementById('main-inputs-div').classList.toggle('hidden');
	});

	document.getElementById('view-grades').addEventListener('click', e => {
		e.preventDefault();
		const currentStudentGrades = localStorage.getItem('studentGrades');
		addStudentGradesToPage(JSON.parse(currentStudentGrades));
	});

	form.addEventListener('submit', e => {
		inputDiv.innerHTML = '';
		e.preventDefault();
		if (validateInput(getValuesFromInputs())) {
			const hwAvg = finalValues['homework-average'];
			const midtermGrade = finalValues['mid-term-exam-score'];
			const finalExamScore = finalValues['final-exam-score'];
			const participation = finalValues['participation'];
			const finalAverage = calculateFinalAverage(hwAvg, midtermGrade, finalExamScore, participation);
			//if input is valid, try to save to localStorage - display a message if student data is successfully added
			studentGrades.push({ studentName, hwAvg, midtermGrade, finalExamScore, participation, finalAverage });
			if (saveToLocalStorage(studentGrades, 'studentGrades')) {
				const successMessage = document.createElement('div');
				successMessage.innerText = 'Student data saved';
				document.body.append(successMessage);
				$(successMessage).fadeOut(2000);
				if (!document.getElementById('student-grades-table').classList.contains('hidden')) {
					const newRow = createRowForGrade({
						studentName,
						hwAvg,
						midtermGrade,
						finalExamScore,
						participation,
						finalAverage
					});
					document.getElementById('student-grades-tbody').append(newRow);
				}
			}
		}
	});

	//functions for event listeners

	function updateStudentName(name) {
		studentName = name;
	}

	function updatePlaceHolderForGradeInputs(name) {
		console.log(placeHolderValues);
		for (let input of inputArray) {
			let placeholderValue = placeHolderValues[input.id];
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
			let placeholderValue = input.getAttribute('placeholder');
			placeholderObj[input.id] = placeholderValue;
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

	function calculateFinalAverage(hwAvg, midtermGrade, finalExamScore, participation) {
		return Math.round(0.5 * hwAvg + 0.2 * midtermGrade + 0.2 * finalExamScore + 0.1 * participation);
		// inputDiv.append(`${studentName}'s final average for the course is ${finalAverage}`);
	}

	function addStudentGradesToPage(grades) {
		const studentGradesTable = document.getElementById('student-grades-table');
		const studentGradesTableBody = document.getElementById('student-grades-tbody');

		if (studentGradesTable.classList.contains('hidden')) {
			for (let grade of grades) {
				let newRow = createRowForGrade(grade);
				studentGradesTableBody.append(newRow);
				studentGradesTable.classList.remove('hidden');
			}
		} else {
			studentGradesTable.innerHTML = `
			<thead>
            <tr>
                <td>Student name</td>
                <td>HW Average</td>
                <td>Midterm score</td>
                <td>Final exam score</td>
                <td>Participation</td>
                <td>Final average</td>
            </tr>
        </thead>
        <tbody id="student-grades-tbody">

        </tbody>
    </table>
			`;
			if (!studentGradesTable.classList.contains('hidden')) {
				studentGradesTable.classList.add('hidden');
			}
		}
	}

	function createRowForGrade(grade) {
		let newRow = template.content.cloneNode(true);
		newRow.getElementById('td-student-name').innerText = grade.studentName;
		newRow.getElementById('td-hw-average').innerText = grade.hwAvg;
		newRow.getElementById('td-midterm-exam-score').innerText = grade.midtermGrade;
		newRow.getElementById('td-final-exam-score').innerText = grade.finalExamScore;
		newRow.getElementById('td-participation').innerText = grade.participation;
		newRow.getElementById('td-final-average').innerText = grade.finalAverage;
		return newRow;
	}

	/*
to-do:
	c. every student grade added to page should have buttons to remove or edit the data
3) refactor so it's class-based + try to add pure functions
4) review data validation -- add tests with Jasmine
*/
});
