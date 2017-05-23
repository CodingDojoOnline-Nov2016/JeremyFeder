// Fahrenheit to Celsius
// Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed in Celsius degrees.
//
// For review, Fahrenheit = (9/5 * Celsius) + 32.

function fahrenheitToCelsius(fDegrees) {
  var cDegrees = (fDegrees - 32) * 5/9;
  console.log(cDegrees);
  return cDegrees;
}

fahrenheitToCelsius(98.6);
fahrenheitToCelsius(32);
