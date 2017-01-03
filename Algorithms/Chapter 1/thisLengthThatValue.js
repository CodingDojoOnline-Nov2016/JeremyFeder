// This Length, That Value
// Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.

function thisThat(num1, num2) {
  if (num1 != num2) {
    var arr = [];
    for (var i = 0; i < num1; i += 1) {
      arr.push(num2);
    }
  }
  else {
    console.log("Jinx!");
  }
  return arr;
}

thisThat(3, 3);
