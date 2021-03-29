const product = multiplyNumbers(false, 5, 9, 13, 17, 21, 25);
[div, p] = createDivWithP();
p.innerHTML = `5 * 9 * 13 * 17 * 21 * 25 is ${product}`;
document.body.append(div);

const sum = addNumbers(false, 5 + 9 + 13 + 17 + 21 + 25);
[div1, p1] = createDivWithP();
p1.innerHTML = `5 + 9 + 13 + 17 + 21 + 25 is ${sum}`;
document.body.append(div1);

const product1 = multiplyNumbers(true, 5, 9, 13, 17, 21, 25);
[div3, p3] = createDivWithP();
p3.innerHTML = `3 * 6 * 9 * 12 * 15 * 18 is ${product}`;
document.body.append(div3);

const sum1 = addNumbers(true, 3, 6, 9, 12, 15, 18);
[div2, p2] = createDivWithP();
p2.innerHTML = `3 + 6 + 9 + 12 + 15 + 18 is ${sum1}`;
document.body.append(div2);

//couldn't get this to work
// $('div').draggable();

function addNumbers(useWhileLoop, ...nums) {
	let total = 0;
	if (useWhileLoop) {
		let index = 0;
		while (nums.indexOf(nums[index]) != -1) {
			total += nums[index];
			index++;
		}
	} else {
		for (let num of nums) {
			total += num;
		}
	}
	return total.toLocaleString();
}

function multiplyNumbers(useWhileLoop, ...nums) {
	nums.unshift(1);
	let total = 1;
	if (useWhileLoop) {
		let index = 0;
		while (nums.indexOf(nums[index]) != -1) {
			total = total * nums[index];
			index++;
		}
	} else {
		for (let num of nums) {
			total = total * num;
		}
	}
	return total.toLocaleString();
}

function createDivWithP() {
	const div = document.createElement('div');
	div.classList.add('text-box');
	const p = document.createElement('p');
	div.append(p);
	return [div, p];
}

// alternate approach
// const ints1 = [5, 9, 13, 17, 21, 25];

// const total1 = ints1.reduce((runningTotal, currentNumber) => runningTotal * currentNumber);
