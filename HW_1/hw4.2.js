const roiTableTbody = document.querySelector('#roi-table-tbody');

const generateTableHTML = (year, amountOnDeposit, interestRate) => {
	return `
    <tr>
    <td>${year}</td>
    <td>$${amountOnDeposit}</td>
    <td>${interestRate}</td>
    </tr>
    `;
};

// The formula to use is : A = P(1 + r)n where

// P is the principal (the initial amount you borrow or deposit)

// r is the annual rate of interest (percentage)

// n is the number of years the amount is deposited

// A is the amount of money accumulated after n years, including interest

const addNewRoiSchedule = (years, initialDeposit, interestRate) => {
	const table = document.createElement('table');
	const tr = document.createElement('tr');
	const th1 = document.createElement('th');
	const th2 = document.createElement('th');
	const th3 = document.createElement('th');
	th1.innerText = 'Year';
	th2.innerText = 'Amount on deposit';
	th3.innerText = 'Interest rate';
	const tbody = document.createElement('tbody');
	const thead = document.createElement('thead');
	table.append(thead);
	thead.append(tr);
	tr.append(th1, th2, th3);
	table.append(tbody);

	let amountOnDeposit = initialDeposit;
	for (let year = 1; year <= years; year++) {
		amountOnDeposit = initialDeposit * Math.pow(1 + interestRate, year);
		tbody.innerHTML += generateTableHTML(year, amountOnDeposit.toFixed(2), interestRate);
	}
	document.body.append(table);
};

addNewRoiSchedule(10, 1000, 0.05);
addNewRoiSchedule(10, 1000, 0.06);
addNewRoiSchedule(10, 1000, 0.07);
