$(document).ready(function(){
  var btn = document.querySelector("#create_course");

  $(btn).click(function(){
    i_id = $(btn).attr('data-instructorID');
    var form = document.createElement("FORM");
    form.setAttribute('id', 'courseInfo');
    form.setAttribute('action', '/system/manage/'+i_id+'/addCourse/');
    form.setAttribute('method', 'GET');
    form.setAttribute('onsubmit', 'check()');
    document.body.appendChild(form);

    var input_title = document.createElement("INPUT");
    input_title.setAttribute('id', 'c_title');
    input_title.setAttribute('type', 'text');
    input_title.setAttribute('name', 'title');


    var input_des = document.createElement("INPUT");
    input_des.setAttribute('id', 'c_des');
    input_des.setAttribute('type', 'text');
    input_des.setAttribute('name', 'description');

    var input_category = document.createElement("INPUT");
    input_category.setAttribute('id', 'input_category');
    input_category.setAttribute('name', 'category');
    input_category.setAttribute('type', 'hidden');

    var input_CECU = document.createElement("INPUT");
    input_CECU.setAttribute('id', 'input_CECU');
    input_CECU.setAttribute('name', 'CECU');
    input_CECU.setAttribute('type', 'hidden');

    form.appendChild(input_title);
    form.appendChild(input_des);
    form.appendChild(input_category);
    form.appendChild(input_CECU);

    select_category = document.createElement("SELECT");
    select_category.setAttribute('id', 'select_category');
    select_category.setAttribute('onchange', 'set_input_category()');
    load_category();



    var select_CECU = document.createElement("SELECT");
    select_CECU.setAttribute('id', 'select_CECU');
    select_CECU.setAttribute('onchange', 'set_input_CECU()');
    var CECU_2 = document.createElement("OPTION");
    CECU_2.innerHTML = '2';
    var CECU_4 = document.createElement("OPTION");
    CECU_4.innerHTML = '4';
    select_CECU.appendChild(CECU_2);
    select_CECU.appendChild(CECU_4);

    input_category.setAttribute('value', select_category.value);
    input_CECU.setAttribute('value', select_CECU.value);

    form.appendChild(select_category);
    form.appendChild(select_CECU);

    var submit_button = document.createElement("INPUT");
    submit_button.setAttribute('type', 'submit');
    form.append(submit_button);

  });

  function set_input_category(){
    var new_category = document.getElementById('select_category').value;
    var input_category = document.getElementById('input_category');
    input_category.setAttribute('value', new_category);
  }

  function set_input_CECU(){
    var new_CECU = document.getElementById('select_CECU').value;
    var input_CECU = document.getElementById('input_CECU');
    input_CECU.setAttribute('value', new_CECU);
  }

  function load_category(){
    var url = '/system/manage/'+i_id+'/loadCategory';
    $.ajax(url,
           {
             dataType: 'json',
             success: function(data, status){
               categories = data.categories;
               for(var i=0;i<categories.length;i++){
                 var c = document.createElement("OPTION");
                 c.innerHTML = categories[i];
                 select_category.appendChild(c);
               }
             }
           }
    );
  }

  $("#courseInfo").submit(function(event){
    event.preventDefault();
    alert("submit the form!");
  });



})
