// First Plus Length
//
// Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

var arr = [4, 2, 3, 4, 5, 8, 10, 20];

function firstPlusLength() {
  var sum = arr[0] + arr.length;
  console.log(sum);
  return sum;
}

firstPlusLength();

//equals 12
