document.addEventListener('DOMContentLoaded', function() {
    //reusing some of the same code from hw2.2.js
    const response = document.createElement('div');
    const form = document.querySelector("#form");
    form.addEventListener('submit', intSubmit);
    function intSubmit(e){
        let posNums = 0, negNums = 0; zeroNums = 0, validInput = true;
        [...form.elements].forEach((input) => {
            if(input.type=="number"){
            inputValue = parseInt(input.value);
            if(inputValue>0){
                posNums++;
            } else if (inputValue<0) {
                negNums ++;
            } else if (inputValue === 0) {
                zeroNums++;
            } else {
                validInput = false;
            }}
        response.innerText = !validInput ? "Please enter a numeric value in all five boxes" :
        "Negative numbers: " + negNums + " Positive numbers: " + posNums + " Zeroes: " + zeroNums;
        });
        e.preventDefault();
        form.appendChild(response);
    }

})