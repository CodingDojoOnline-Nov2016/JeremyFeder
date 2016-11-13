$(document).ready(function() {

// var jeremy = function(x, y) {
//   return x+y;
// }
//
// jeremy(3, 5);

  // alert('you are now working with jQuery');
  $('a.mylink').click(function(){
    alert('You actually clicked me!!');
  });

  $('#addclass button').click(function() {
    $('#addclass p:last').addClass('selected highlight');
  });

  $('#append button').click(function() {
    $('#appendP').append("New Paragraph");
  });

  $("#fades .button1").click(function() {
    $("#automotive").fadeOut("slow", function() {
    });
  });

  $("#fades .button2").click(function() {
    $("#automotive").fadeIn("slow", function() {
    });
  });

})
