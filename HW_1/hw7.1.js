for (let radioButton of Array.from(document.getElementsByName('font-size'))) {
	radioButton.addEventListener('click', e => {
		changeFontSize(e.target.value);
	});
}

document.getElementById('font-select').addEventListener('change', e => {
	changeFont(e.target.value);
});

for (let checkbox of Array.from(document.getElementsByName('checkbox-style'))) {
	checkbox.addEventListener('click', e => {
		toggleCheckboxAction(e.target.id);
	});
}

function changeFont(font) {
	//accepts a font name chosen via a select menu and changes DOM accordingly
	document.body.className = '';
	if (!['', undefined, 'Arial'].includes(font)) {
		document.body.classList.add(font);
	} else {
		document.body.classList.add('default');
	}
}

function changeFontSize(fontSize) {
	//accepts a font size selected from a radio button and changes DOM accordingly
	document.getElementById('sample-text').style.fontSize = fontSize.toString() + 'px';
}

function toggleCheckboxAction(value) {
	//accepts a value from a selected checkbox, and toggles on or off a specific class by referencing code snippets in checkboxActions object
	eval(checkboxActions[value]);
}

const checkboxActions = {
	italics: `document.getElementById('sample-text').classList.toggle('italics');`,
	'increase-spacing': `document.getElementById('sample-text').classList.toggle('letter-spacing');`,
	bold: `document.getElementById('sample-text').classList.toggle('bold');`
};

function getComputedProperty(element, property) {
	return window.getComputedStyle(element, null).getPropertyValue(property);
}
