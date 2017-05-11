// You Say It’s Your Birthday
//
// If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....",
//
// Example: given yourBirthday(4,19) or yourBirthday(19,4)

var month = 1;
var day = 12;

function yourBirthday(month, day) {
  if ((month === 1 && day === 12) || (month === 12 && day === 1)) {
    console.log("How did you know?");
  } else {
    console.log("Just another day....");
  }
};

yourBirthday(1, 12);
yourBirthday(12, 1);
yourBirthday(2, 19);
yourBirthday(4, "cat");
