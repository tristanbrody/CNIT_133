document.addEventListener('DOMContentLoaded', function() {
//create element that will show response upon submitting inputs
const response = document.createElement('div');
//define form element and add event listener for submission
const form = document.querySelector("#form");
form.addEventListener('submit', intSubmit);
//function that runs for event listener
function intSubmit(e){
    let sum = 0, avg = 0, product = 0, largestNum = 0, numInputs = 0, prevNum = null; validInput = true;
    $(response).fadeIn();
    [...form.elements].forEach((input) => {
        if(input.type=="number"){
        inputValue = parseInt(input.value);
            if(input.value==""){
                response.innerText="Please enter a value for all three inputs";
                validInput = false;
            } else {
                sum += inputValue;
                numInputs ++;
                if(input !== form.elements[0]){
                    product = inputValue * product;
                    prevNum = inputValue;
                } else {
                    prevNum = inputValue;
                    product = inputValue * 1;
                }
                if(inputValue>largestNum){
                    largestNum = inputValue;
                }
            }
        }
    });
    e.preventDefault();
    if(validInput){
        avg = sum/numInputs;
        response.innerText = "Sum: " + sum + " Average: " + avg + " Product: " + product + 
        " Largest Number: " + largestNum;
    }
    form.appendChild(response);
    $(response).fadeOut(2000);
}
})
