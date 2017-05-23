// Values Greater than Second, Generalized
//
// Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?

var arr = [1,2,3,4,5];

function valGreatGen(arr) {
  var newArr = [];
  var count = 0;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] > arr[1]) {
      newArr.push(arr[i]);
      count++;
    }
  }
  console.log(newArr, count);
  return (newArr, count);
}

valGreatGen(arr);


// or if array is only 1 index long and also to do away with the count

var arr = [1,2,3,4,5];
var arr2 = [3];

function valGreatGen(arr) {
  if (arr.length > 1) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
      if (arr[i] > arr[1]) {
        newArr.push(arr[i]);    }
    }
    console.log(newArr, newArr.length);
    return (newArr, newArr.length);
  } else {
    console.log("Array must have more than one index.");
  }
}

valGreatGen(arr);
valGreatGen(arr2);
