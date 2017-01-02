// Counting, the Dojo Way
// Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

function countDojo() {
  for (var i = 1; i <= 100; i += 1) {
    if ((i % 5 === 0) && (i % 10 === 0)) {
      console.log("Coding Dojo");
    }
    else if (i % 5 === 0) {
      console.log("Coding");
    }
    else {
      console.log(i);
    }
  }
}

countDojo();
