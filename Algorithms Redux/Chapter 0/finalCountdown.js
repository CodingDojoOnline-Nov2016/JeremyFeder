// The Final Countdown
//
// This is based on “Flexible Countdown”. The parameter names are not as helpful, but the problem is essentially identical; don’t be thrown off! Given 4 parameters (param1,param2,param3,param4), print the multiples of param1, starting at param2 and extending to param3. One exception: if a multiple is equal to param4, then skip (don’t print) that one. Do this using a WHILE loop.
//
// Example: Given (3,5,17,9), print 6,12,15 (which are all of the multiples of 3 between 5 and 17, except for the value 9).

function finalCount(mult1, min2, max3, except4) {
  while (min2 <= max3) {
    if ((min2 != except4) && (min2 % mult1 === 0)) {
      console.log(min2);
    }
  min2++;
  }
};

finalCount(3, 5, 17, 9);
