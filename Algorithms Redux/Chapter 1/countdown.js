// Countdown
//
// Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zero’th element) down to 0 (as the last element). How long is this array?

function countdown(inputNumber) {
  var arr = [];
  for (var i = inputNumber; i >= 0; i--) {
    arr[arr.length] = i;
  }
  console.log(arr, "Length of array is: " + arr.length);
}

countdown(4);
