// Values Greater than Second
// For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.

var arr = [1,3,5,7,9,13]

function valGreaterSecond() {
  countGreater = 0;
  for (var i = 0; i < arr.length; i += 1) {
    if (arr[1] < arr[i]) {
      countGreater += 1;
      console.log(arr[i]);
    }
  }
  return countGreater;
}

valGreaterSecond();
