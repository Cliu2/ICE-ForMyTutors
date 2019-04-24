$(document).ready(function(){
  var btn = document.querySelector("#requestAddComponent");
  var container = document.getElementById("available_components");
  var content = false;

btn.onclick = function(){
    var c_id = $(btn).attr("data-cid");
    var i_id = $(btn).attr("data-uid");
    var m_id = $(btn).attr("data-mid");
    var form = createForm(c_id, i_id, m_id);
    if(content==false){
      container.append(form);
      content = true;
    }
    load_components(c_id, m_id);
    set_input_component();
  }
})

function createForm(c_id, i_id, m_id){
  var form = document.createElement("FORM");
  form.setAttribute('method', 'GET');
  form.setAttribute('action', '/system/manage/'+c_id+'/'+m_id+'/addComponent/');

  select_component = document.createElement("SELECT");
  select_component.setAttribute('id', 'select_component');
  select_component.setAttribute('onchange', 'set_input_component()');

  var input_order = document.createElement("INPUT");
  input_order.setAttribute('id', 'input_order');
  input_order.setAttribute('name', 'order');
  input_order.setAttribute('type', 'text');
  input_order.setAttribute('defaultValue', '-1');
  input_order.setAttribute('placeholder', 'order (optional)');

  input_component = document.createElement("INPUT");
  input_component.setAttribute('id', 'input_component');
  input_component.setAttribute('name', 'component_name');
  input_component.setAttribute('type', 'hidden');

  var input_submit = document.createElement("INPUT");
  input_submit.setAttribute('type', 'submit');

  form.appendChild(select_component);
  form.appendChild(input_order);
  form.appendChild(input_component);
  form.appendChild(input_submit);
  return form;

}

function load_components(c_id, m_id){
  var url = '/system/manage/'+c_id+'/'+m_id+'/loadComponents/';
  $.ajax(url,
         {
           dataType: 'json',
           success: function(data, status){
             components = data.components;
             for(var i=0;i<components.length;i++){
               var c = document.createElement("OPTION");
               c.innerHTML = components[i];
               select_component.appendChild(c);
             }
             // set_input_component();
             input_component.setAttribute('value', components[0]);
           }
         }
  );
}

set_input_component = function(){
  var component_name = document.getElementById("select_component").value;
  input_component.setAttribute('value', component_name);
}
