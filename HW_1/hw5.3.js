const stateForm = document.getElementById('form-state-info');

stateForm.addEventListener('submit', e => {
	e.preventDefault();
	//remove previous output
	document.querySelector('.output-container').innerText = '';

	//convert all input to lower case
	let inputValue = e.target[0].value.toLowerCase();

	//get state data based on input value. If input is abbreviated statename, reference the stateKeyMapping object to convert to full state name
	let convertedInput = inputValue in stateData ? stateData[inputValue] : stateData[stateKeyMapping[inputValue]];

	//add output for states that aren't in table
	if (convertedInput === undefined && checkIfInputIsAState(inputValue)) {
		document.querySelector('.output-container').innerText = getOutput(inputValue, true);
	} else {
		//add output for other scenarios
		document.querySelector('.output-container').innerText = getOutput(convertedInput);
	}
});

function checkIfInputIsAState(input) {
	for (const [key, value] of Object.entries(stateKeyMapping)) {
		if ([key, value].includes(input)) return true;
	}
	return false;
}
function getOutput(inputValue, stateNotInTable = false) {
	//if true is passed in, we don't have data in the table yet for the state passed in. Otherwise, either undefined or the relevant state object is passed in
	if (stateNotInTable) return "Sorry, we don't currently have data for this state.";
	if (inputValue === undefined)
		return 'Invalid input. Input should be a state (either two letter or full state name is accepted)';
	return `Here are some fun facts on the state:
State abbreviation: ${inputValue.stateAbbreviation}
State Name: ${inputValue.stateName}
Capital: ${inputValue.capital}
Population: ${inputValue.population}
`;
}

const stateData = {
	alabama: {
		stateAbbreviation: 'AL',
		stateName: 'Alabama',
		capital: 'Montgomery',
		population: '4,903,185'
	},
	alaska: {
		stateAbbreviation: 'AK',
		stateName: 'Alaska',
		capital: 'Juneau',
		population: '731,545'
	},
	arizona: {
		stateAbbreviation: 'AZ',
		stateName: 'Arizona',
		capital: 'Phoenix',
		population: '7,278,717'
	},
	arkansas: {
		stateAbbreviation: 'AR',
		stateName: 'Arkansas',
		capital: 'Little Rock',
		population: '3,017,825'
	},
	california: {
		stateAbbreviation: 'CA',
		stateName: 'California',
		capital: 'Sacramento',
		population: '39,512,223'
	},
	colorado: {
		stateAbbreviation: 'CO',
		stateName: 'Colorado',
		capital: 'Denver',
		population: '5,758,736'
	}
};

const stateKeyMapping = {
	al: 'alabama',
	ak: 'alaska',
	as: 'american samoa',
	az: 'arizona',
	ar: 'arkansas',
	ca: 'california',
	co: 'colorado',
	ct: 'connecticut',
	de: 'delaware',
	dc: 'district of columbia',
	fm: 'federated states of micronesia',
	fl: 'florida',
	ga: 'georgia',
	gu: 'guam',
	hi: 'hawaii',
	id: 'idaho',
	il: 'illinois',
	in: 'indiana',
	ia: 'iowa',
	ks: 'kansas',
	ky: 'kentucky',
	la: 'louisiana',
	me: 'maine',
	mh: 'marshall islands',
	md: 'maryland',
	ma: 'massachusetts',
	mi: 'michigan',
	mn: 'minnesota',
	mw: 'mississippi',
	mo: 'missouri',
	mt: 'montana',
	ne: 'nebraska',
	nv: 'nevada',
	nh: 'new nampshire',
	nj: 'new jersey',
	nm: 'new mexico',
	ny: 'new york',
	nc: 'north carolina',
	nd: 'north dakota',
	mp: 'northern mariana islands',
	oh: 'ohio',
	ok: 'oklahoma',
	or: 'oregon',
	pw: 'palau',
	pa: 'pennsylvania',
	pr: 'puerto rico',
	ri: 'rhode island',
	sc: 'south carolina',
	sd: 'south dakota',
	tn: 'tennessee',
	tx: 'texas',
	ut: 'utah',
	vt: 'vermont',
	vi: 'virgin islands',
	va: 'virginia',
	wa: 'washington',
	wv: 'west virginia',
	wi: 'wisconsin',
	wy: 'wyoming'
};
