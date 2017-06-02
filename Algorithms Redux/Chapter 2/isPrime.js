// Is Prime
// Return whether a given integer is prime. Prime numbers are only evenly divisible by themselves and 1. Many highly optimized solutions exist, however, for now, just create one that is easy to understand and debug.


function isPrime(value) {
  for(var i = 2; i < value; i++) {
    if(value % i === 0) {
      console.log(false);
      return false;
    }
  }
  console.log(true);
  return true;
}

isPrime(5);
