// Values Greater than Second, Generalized
// Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?

var arr = [1,3,5,7,9,13];
var arr2 = [2,1,3,4,5,6,7,8,9,10];
var arr3 = [3,5,3,4,7,8,3,4,6,88,99,22,1,3];
var arr4 = [1];

function valGreaterSecond(arr) {
  var inputArr = [];
  for (var i = 0; i < arr.length; i += 1) {
    if (arr[1] < arr[i]) {
      inputArr.push(arr[i]);
    }
  }
  console.log(inputArr.length);
}

valGreaterSecond(arr);
valGreaterSecond(arr2);
valGreaterSecond(arr3);
valGreaterSecond(arr4);

//if the array is one element long

var arr = [1,3,5,7,9,13];
var arr2 = [2,1,3,4,5,6,7,8,9,10];
var arr3 = [3,5,3,4,7,8,3,4,6,88,99,22,1,3];
var arr4 = [1];

function valGreaterSecond(arr) {
  if (arr.length > 1) {
    var inputArr = [];
    for (var i = 0; i < arr.length; i += 1) {
      if (arr[1] < arr[i]) {
        inputArr.push(arr[i]);
      }
    }
    console.log(inputArr.length);
  }
  else {
    console.log("Please enter an array with more than one index value.")
  }
}

valGreaterSecond(arr);
valGreaterSecond(arr2);
valGreaterSecond(arr3);
valGreaterSecond(arr4);
