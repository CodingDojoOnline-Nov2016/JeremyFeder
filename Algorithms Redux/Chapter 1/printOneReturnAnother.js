// Print One, Return Another
// Build a function that takes array of numbers. The function should print second-to-last value in the array, and return first odd value in the array.

function printOneRetAnother(arr) {
  console.log(arr[arr.length - 2]);
  var i = 0;
  while (arr[i] % 2 != 1) {
    i++;
  }
  return arr[i];
}

var arr = [4, 6, 2, 8, 10, 3, 5, 0, 37, 6];

printOneRetAnother(arr);
