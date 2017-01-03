// Countdown
// Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zero’th element) down to 0 (as the last element). How long is this array?

function countdown(input) {
  var arr = [];
  for (var i = input; i >= 0; i -= 1) {
    arr[arr.length] = i;
  }
  console.log(arr, "*** " + arr.length + " ***");
  return arr;
}

countdown(7);
