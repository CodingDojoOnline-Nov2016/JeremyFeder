// Multiples of Six
// Print multiples of 6 up to 60,000, using a WHILE.

function multsOfSix() {
  var i = 6;
  while (i <= 60000) {
    if (i % 6 === 0) {
      console.log(i);
    }
    i += 1;
  }
}

multsOfSix();
