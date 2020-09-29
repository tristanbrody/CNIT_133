let form = document.querySelector('#input-form');
let itemPrices = Array.from(document.querySelectorAll("[data-type='price']"));
let itemInputs = Array.from(document.querySelectorAll("input[id*='item']"));
let allOutputs = Array.from(document.querySelectorAll('.sold-output'));

let itemObj = {};

form.addEventListener('submit', e => {
	e.preventDefault();
	clearOutputs();
	itemObj = {};
	getItemPrices();
	document.querySelector('.input-div').innerText = '';
	if (validateInputs()) {
		getNumberSold();
		getTotalSalesByItem();
		outputNumberSold();
		outputTotalSold();
		outputGrandTotalSold();
		outputGrandTotalEarnings();
	}
});

function validateInputs() {
	for (let input of itemInputs) {
		if (onlyNums(input.value)) {
			return true;
		} else {
			let linebreak = document.createElement('br');
			//prettier-ignore
			document.querySelector('.input-div').append(`Please correct your entry for ${input.dataset.name}`, linebreak);
			return false;
		}
	}
}

function getItemPrices() {
	for (let item of itemPrices) {
		itemObj[`${item.dataset.item}price`] = item.innerText.replace(/^\$/, '');
	}
}

function getNumberSold() {
	for (let input of itemInputs) {
		itemObj[`${input.id}numSold`] = input.value;
		itemObj['totalNumber'] =
			itemObj['totalNumber'] === undefined
				? parseInt(input.value)
				: (itemObj['totalNumber'] += parseInt(input.value));
	}
}

function getTotalSalesByItem() {
	let i = 1;
	for (const [key, value] of Object.entries(itemObj)) {
		if (itemObj[`item-${i}numSold`] === undefined) break;
		itemObj[`item-${i}totalSold`] = itemObj[`item-${i}numSold`] * itemObj[`item-${i}price`];
		itemObj['totalEarnings'] =
			itemObj['totalEarnings'] === undefined
				? parseInt(itemObj[`item-${i}totalSold`])
				: (itemObj['totalEarnings'] += parseInt(itemObj[`item-${i}totalSold`]));

		i++;
	}
}

function outputNumberSold() {
	let numSoldLineItems = Array.from(document.querySelectorAll("[data-type='number-sold']"));
	for (let i = 0; i < numSoldLineItems.length; i++) {
		if (numSoldLineItems[i].dataset.item === `item-${i + 1}`) {
			numSoldLineItems[i].value = itemObj[`item-${i + 1}numSold`];
		}
	}
}

function outputTotalSold() {
	let totalSoldLineItems = Array.from(document.querySelectorAll("[data-type='total-sold']"));
	for (let i = 0; i < totalSoldLineItems.length; i++) {
		if (totalSoldLineItems[i].dataset.item === `item-${i + 1}`) {
			totalSoldLineItems[i].value = itemObj[`item-${i + 1}totalSold`].toFixed(2);
		}
	}
}

function outputGrandTotalSold() {
	document.querySelector("[data-type='grand-total']").value = itemObj['totalNumber'];
}

function outputGrandTotalEarnings() {
	document.querySelector("[data-type='grand-total-weekly']").value = itemObj['totalEarnings'];
}

function clearOutputs() {
	for (let i = 0; i < allOutputs.length; i++) {
		allOutputs[i].innerText = '';
		allOutputs[i].value = '';
	}
}
