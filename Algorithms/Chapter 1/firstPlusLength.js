// First Plus Length
// Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

var arr = [1, 2, 3, 4];

function firstPlus() {
  var sum = arr[0] + arr.length;
  console.log(sum);
  return sum;
}

firstPlus();
