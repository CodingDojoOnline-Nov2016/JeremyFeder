// Fit the First Value
// Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!"; if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".

function fitFirst(arr) {
  if (arr[0] > arr.length) {
    console.log("Too big!");
  }
  else if (arr[0] < arr.length) {
    console.log("Too small!")
  }
  else {
    console.log("Just right!")
  }
}

var arrBig = [20, 34, 4];
var arrSmall = [1, 4, 6, 7];
var arrRight = [2, 6];

fitFirst(arrBig);
fitFirst(arrSmall);
fitFirst(arrRight);
