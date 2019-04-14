$(document).ready(function(){
  var btn = document.querySelector("#requestAddComponent");
  var displayArea = document.querySelector("#available_components");

  btn.click(function(){
    var c_id = $(btn).attr("data-cid");
    var i_id = $(btn).attr("data-uid");
    var m_id = $(btn).attr("data-mid");
    $.ajax({
      url: '/system/manage/'+i_id+'/'+c_id+'/'+m_id+'/',
      success: function(result){
        var p = "";
        
      }
    });
  })
})
