const select1 = document.getElementById('select-language-links');
const select2Button = document.getElementById('button-coding-links');

select1.addEventListener('change', e => {
	if (e.target.value != '') window.open(e.target.value, '_blank');
});

select2Button.addEventListener('click', e => {
	e.preventDefault();
	if (e.target.form[0].value != '') window.open(e.target.form[0].value, '_blank');
});
