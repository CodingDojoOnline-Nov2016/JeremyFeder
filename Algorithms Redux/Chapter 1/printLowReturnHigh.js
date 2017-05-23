// Print Low, Return High
// Create a function that takes array of numbers. The function should print the lowest value in the array, and return the highest value in the array.

function prtLowReturnHigh(arr) {
  var lowest = arr[0];
  var highest = arr[0];
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] < lowest) {
      lowest = arr[i];
    } else if (arr[i] > highest) {
        highest = arr[i];
      }
  }
  console.log(lowest);
  return highest;
}

var arr = [3,2,1,4,5];
prtLowReturnHigh(arr);
