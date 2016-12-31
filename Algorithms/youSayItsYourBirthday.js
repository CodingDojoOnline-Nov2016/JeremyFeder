// You Say It’s Your Birthday
// If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....",
//
// Example: given yourBirthday(4,19) or yourBirthday(19,4)

function sayBirthday(x, y) {
  var month = 1;
  var day = 12;
  // if (((x === month) && (y === day)) || ((y === month) && (x === day))) {
  if ((x === month && y === day) || (y === month && x === day)) {
    console.log("How did you know?");
  }
  else {
    console.log("Just another day....");
  }
}
sayBirthday(1, 12);
sayBirthday(12, 1);
sayBirthday(4, 4);
