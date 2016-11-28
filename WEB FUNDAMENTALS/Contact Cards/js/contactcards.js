$(document).ready(function() {

  $('form').submit(function () {

    var fields = {
      "firstName": $('#first-name').val(),
      "lastName": $('#last-name').val(),
      "descript": $('#description').val()
    }  //made an object.

    var  htmlString = ""
    htmlString += "<div>"
    htmlString += "<h2>" + fields.firstName + " " + fields.lastName + "</h2><p>" + 'Click on me for a description!' + "</p>"

    $(".cards").append(htmlString)

    $(document).on('click', '.cards', function(){
      // alert('you clicked a button!');
      $(".cards").append(fields.descript);
    });


    return false;

  })

})
