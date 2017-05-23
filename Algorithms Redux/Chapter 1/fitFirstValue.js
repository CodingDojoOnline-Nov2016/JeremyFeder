// Fit the First Value
//
// Your function should accept an array. If the value at [0] is greater than array’s length, print "Too big!"; if the value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".

var arrBig = [10, 3, 5, 7];
var arrSmall = [1, 3, 4, 8, 9];
var arrRight = [3, 2, 1];


function fitFirstVal(arr) {
  if (arr[0] > arr.length) {
    console.log("Too big!");
  }
  else if (arr[0] < arr.length) {
    console.log("Too small!");
  }
  else {
    console.log("Just right!");
  }
}

fitFirstVal(arrBig);
fitFirstVal(arrSmall);
fitFirstVal(arrRight);
