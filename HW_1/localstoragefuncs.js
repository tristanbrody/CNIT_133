function saveToLocalStorage(item, itemName = 'item') {
	try {
		localStorage.setItem(itemName, JSON.stringify(item));
		return true;
	} catch (err) {
		console.log(`error is ${err}`);
		return false;
	}
}
