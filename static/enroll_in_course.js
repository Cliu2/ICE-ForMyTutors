$(document).ready(function(){
  var disabled = $("#enroll").attr('data-disabled');

  $("#enroll").click(function(){
    if(disabled==true){
      alert("You cannot enroll in the same course twice!");
    }
    else{
      url = '/system/view/' + $("#enroll").attr('data-learnerID') + '/enrollInCourse/' + $("#enroll").attr('data-courseID') + '/';
      $.get(
        url
      );
    }
  });
})
