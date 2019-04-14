$(document).ready(function(){
  var select_category = document.querySelector("#select_category");

  var l_id = $("#course_list").attr('data-learnerID');
  load_category();
  var courses = document.getElementsByClassName("course");


  var cc = [];
  for(var i=0;i<courses.length;i++){
    cc.push({
      key: $(courses[i]).attr('data-category'),
      value: courses[i].innerHTML
    });
  }


  function load_category(){
    var url = '/system/view/'+l_id+'/loadCategoryForLearner/';
    $.ajax(
      url,
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


  $("#filterBy").change(function(){
    var filter_by = document.getElementById("filterBy").value;
    var course_list = document.getElementById("course_list");
    if(filter_by!="name"){
      course_list.innerHTML = "";
      for(var i=0;i<cc.length;i++){
        if(cc[i].key==filter_by){
          // alert("match!");
          var li = document.createElement("LI");
          li.innerHTML = cc[i].value;
          li.setAttribute('class', 'course');
          li.setAttribute('data-category', cc[i].key);
          course_list.appendChild(li);
        }
      }
    }
    else{
      course_list.innerHTML = "";
      for(var i=0;i<cc.length;i++){
        var li = document.createElement("LI");
        li.innerHTML = cc[i].value;
        li.setAttribute('class', 'course');
        li.setAttribute('data-category', cc[i].key);
        course_list.appendChild(li);
      }
    }
  });


})
