// Setting and Swapping
// Set variable myNumber to 42. Set variable myName to your name. Now swap myNumber into myName & vice versa.

// var myNumber = 42;
// var myName = "Jeremy";

function setSwap(x, y) {
  var temp = x;
  x = y;
  y = temp;
  console.log(x, y);
}

setSwap(42, "Jeremy");
