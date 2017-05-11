// Print and Count
//
// Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.

function printCount() {
  var count = 0;
  for (var int = 512; int <= 4096; int++) {
    if (int % 5 === 0) {
      count ++;
      console.log(int + " " + count);
    }
  }
};

printCount();
