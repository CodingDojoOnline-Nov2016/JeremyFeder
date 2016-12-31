// Print and Count
// Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.

function printCount() {
  var count = 0;
  for (var i = 512; i <= 4096; i += 1) {
    if (i % 5 === 0) {
      console.log(i);
      count += 1
    }
  }
  console.log("The Count is: "+count);
}
 printCount();
