$(document).ready(function(){
  var btn = document.querySelector("#create_course");
  var form = document.querySelector("#courseInfo");

  set_input_category = function(){
    var new_category = document.getElementById('select_category').value;
    var input_category = document.getElementById('input_category');
    input_category.setAttribute('value', new_category);
  }
  set_input_CECU = function(){
    // alert("set new CECU!");
    var new_CECU = document.getElementById('select_CECU').value;
    var input_CECU = document.getElementById('input_CECU');
    input_CECU.setAttribute('value', new_CECU);
  }


  $(btn).click(function(){
    i_id = $(btn).attr('data-instructorID');
    var url = '/system/manage/createCourse/';

    $("#form_container").remove();

    var form = createForm(url);
    document.body.appendChild(form);
    load_category();
  });



  function load_category(){
    var url = '/system/manage/loadCategory/';
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
               set_input_category();
               set_input_CECU();
             }
           }
    );
  }

  function load_course_info(i_id, c_id){
    load_category();
    var url = '/system/manage/loadCourseInfo/'+c_id+'/';
    $.ajax(url,
          {
            dataType: 'json',
            success: function(data, status){
              $("#c_title").attr('value', data.title);
              $("#c_des").attr('value', data.description);
              $("#input_category").attr('value', data.category);
              $("#input_CECU").attr('value', data.CECU);
              $("#select_category").attr('value', data.category);
              $("#select_CECU").attr('value', data.CECU);
            }
          });
  }

  $(".editCourse").click(function(e){
    $("#form_container").remove();
    c_id = $(e.target).attr('data-courseID');
    i_id = $(e.target).attr('data-instructorID');
    var url = '/system/manage/editCourse/'+c_id+'/';
    var form = createForm(url);
    e.target.parentNode.appendChild(form);
    // load_category();

    load_course_info(i_id, c_id);

  });

  function createForm(url){
    var form_container = document.createElement("DIV");
    form_container.setAttribute("id", "form_container");

    var form = document.createElement("FORM");
    form.setAttribute('id', 'courseInfo');
    form.setAttribute('action', url);
    form.setAttribute('method', 'GET');

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

    select_category = document.createElement("SELECT");
    select_category.setAttribute('id', 'select_category');
    // load_category();
    select_CECU = document.createElement("SELECT");
    select_CECU.setAttribute('id', 'select_CECU');

    var CECU_2 = document.createElement("OPTION");
    CECU_2.innerHTML = '2';
    var CECU_4 = document.createElement("OPTION");
    CECU_4.innerHTML = '4';
    select_CECU.appendChild(CECU_2);
    select_CECU.appendChild(CECU_4);

    select_category.setAttribute('onchange', 'set_input_category();');
    select_CECU.setAttribute('onchange', 'set_input_CECU()');

    var submit_button = document.createElement("INPUT");
    submit_button.setAttribute('type', 'submit');

    var cancel_button = document.createElement("BUTTON");
    cancel_button.setAttribute('class', 'cancel');
    cancel_button.setAttribute('onclick', 'clearForm()');
    cancel_button.innerHTML='cancel';

    form.appendChild(input_title);
    form.appendChild(input_des);
    form.appendChild(input_category);
    form.appendChild(input_CECU);
    form.appendChild(select_category);
    form.appendChild(select_CECU);
    form.append(submit_button);

    form_container.append(form);
    form_container.append(cancel_button);

    return form_container;


  }

  clearForm = function(){
    $("#form_container").remove();
  }

})
