$(document).ready(function() {

  // alert('you are now working with jQuery');
  $('a.mylink').click(function(){
    alert('You actually clicked me!!');
  });

  $('#addClass').click(function() {
  $('#addClassP:last').addClass('selected highlight');
  });

  $('#append').click(function() {
  $('#appendP').append("New Paragraph");
  });



})
