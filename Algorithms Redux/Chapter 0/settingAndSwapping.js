// // Setting and Swapping
//
// // Set variable myNumber to 42. Set variable myName to your name. Now swap myNumber into myName & vice versa.

var myNumber = 42;
var myName = "Jeremy";
// console.log(myNumber, myName);

function setSwap (myNumber, myName) {
  var temp = myNumber;
  myNumber = myName;
  myName = temp;
  console.log(myNumber, myName);
}

setSwap(myNumber, myName);
setSwap(myName, myNumber);
setSwap(myNumber, myName);
