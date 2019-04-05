$(document).ready(function(){
  var btn = document.querySelector("#create_module");
  var request_add = document.querySelector("#request_add");
  var cm_exist = false;

  btn.onclick = function(){
    var i_id = $(btn).attr('data-uid');
    var c_id = $(btn).attr('data-courseID');
    if(cm_exist==false){
      var p2 = 'Module Title: <input id="input_m_title" type="text" name="title"></input>';
      var p4 = '<input type="hidden" name="c_id" value='+c_id+'>';
      var p5 = '<input type="hidden" name="i_id" value='+i_id+'>';
      var p6 = '<input type="submit"></input>';
      $("#module_info").append(p2, p4, p5, p6);
      $("#module_info").attr("action", '/system/manage/'+i_id+'/'+c_id+'/add/');
      cm_exist = true;
    }
  }

  var form = $("#module_info");


})
