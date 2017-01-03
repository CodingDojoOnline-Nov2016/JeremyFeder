// Countdown By Fours
// Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.

function countdownFours() {
  var num = 2016;
  while (num > 0) {
    console.log(num);
    num -= 4;
  }
}

countdownFours();
