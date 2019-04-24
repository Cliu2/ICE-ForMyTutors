$(document).ready(function(){
  $("#drop").click(function(e){
    var c_id = $("#drop").attr("data-cid");
    var confirmation = confirm("Do you confirm you want to drop this course?");
    if(confirmation==true){
      var url = "/system/view/dropCourse/" + c_id + "/";
      $.get(url,
            {
              success: location.reload(),
            }
      );
    }
  });
})
