// Celsius to Fahrenheit
// Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, and returns the equivalent temperature expressed in Fahrenheit degrees.
//
// (optional) Do Fahrenheit and Celsius values equate at a certain number? Scientific calculation can be complex, so for this challenge just try a series of Celsius integer values starting at 200, going downward (descending), checking whether it is equal to the corresponding Fahrenheit value.

function celsiusToFahrenheit(cDegrees) {
  var fDegrees = (9/5 * cDegrees) + 32;
  console.log(fDegrees);
  return fDegrees;
}

celsiusToFahrenheit(0);

//optional part

function findEquilibrium() {
	fDegrees = 0;
	for (var i = 200; i != fDegrees; i -= 1) {
		fDegrees = ((i - 1) * 9/5) + 32;
	}
	console.log(i + " degrees is the equilibrium point.");
}

findEquilibrium();
