$(document).ready(function(){
  var btn = document.querySelector("#create_module");
  var request_add = document.querySelector("#request_add");
  var cm_exist = false;

  btn.onclick = function(){
    var i_id = $(btn).attr('data-uid');
    var c_id = $(btn).attr('data-courseID');
    if(cm_exist==false){
      var p2 = 'Module Title: <input id="input_m_title" type="text" name="title"></input><br>';
      var p3 = 'Module Order (optional):<input id="input_order" type="text" name="order" value="-1"></input><br>';
      var p4 = '<input type="hidden" name="c_id" value='+c_id+'>';
      var p5 = '<input type="hidden" name="i_id" value='+i_id+'>';
      var p6 = '<input type="submit"></input>';
      $("#module_info").append(p2, p3, p4, p5, p6);
      $("#module_info").attr("action", '/system/manage/'+c_id+'/createModule/');
      cm_exist = true;
      var form_container = document.getElementById("form_container");
      var cancel_button = document.createElement("BUTTON");
      cancel_button.innerHTML = 'cancel';
      cancel_button.setAttribute('onclick', 'clearForm()');
      cancel_button.setAttribute('id', 'cancelCreation');
      form_container.appendChild(cancel_button);
    }
    // var form_container = document.getElementById("form_container");
    // var cancel_button = document.createElement("BUTTON");
    // cancel_button.innerHTML = 'cancel';
    // cancel_button.setAttribute('onclick', 'clearForm()');
    // cancel_button.setAttribute('id', 'cancelCreation');
    // form_container.appendChild(cancel_button);
  }

  var form = $("#module_info");

  clearForm = function(){
    // document.getElementById("module_info").innerHTML='';
    // alert(document.getElementById("module_info").innerHTML);
    document.getElementById("module_info").innerHTML = "";
    $("#cancelCreation").remove();
    cm_exist = false;


  }
})
