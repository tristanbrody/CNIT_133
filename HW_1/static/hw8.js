const nameInput = document.querySelector('input#first-name');
const hintOutput = document.querySelector('#hint-output');

nameInput.addEventListener('keyup', async function (e) {
	let userInput = e.target.value;
	const hint = await getHint(userInput);
	if (hint['hint_available'] && userInput !== '') {
		addHintToDOM(hint['hint'].join(', '));
	} else {
		addHintToDOM('');
	}
});

async function getHint(firstname) {
	let data = await fetch(
		'/gethint?' +
			new URLSearchParams({
				firstname
			}),
		{ method: 'get' }
	);
	return data.json();
}

function addHintToDOM(hint) {
	hintOutput.innerText = hint;
}
