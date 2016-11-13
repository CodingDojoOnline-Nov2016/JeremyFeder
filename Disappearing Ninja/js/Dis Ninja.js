$(document).ready(function() {

  $("img").click(function() {
    $(this).hide("slow", function() {
    });
  });

  $("button").click(function() {
    $("img").show("slow", function() {
    });
  });

})
