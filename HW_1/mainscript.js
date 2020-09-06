document.addEventListener("DOMContentLoaded", function() {
const incompleteHWLinks = document.querySelectorAll('.coming-soon');
for(const a of incompleteHWLinks) {
a.addEventListener('mouseover', function() {
    a.innerText = 'Coming soon!';
})

}
})