$(function() {


        $.ajaxSetup({
            success:function(response){
                clear_messages();
                
                if(response.status == '1'){
                    set_success(response.message);
                }else if(response.status == '0'){
                    set_errors(response.errors);
                }
            },
                
            error: function(jqXHR, exception) {

                if (jqXHR.status === 0) {
                    alert('Not connect.\n Verify Network.');
                } else if (jqXHR.status == 403) {
                        alert('Forbidden. [403]');
                } else if (jqXHR.status == 404) {
                    alert('Requested page not found. [404]');
                } else if (jqXHR.status == 500) {
                    alert('Internal Server Error [500].');
                } else if (exception === 'parsererror') {
                    alert('Requested JSON parse failed.');
                } else if (exception === 'timeout') {
                    alert('Time out error.');
                } else if (exception === 'abort') {
                    alert('Ajax request aborted.');
                } else {
                    alert('Uncaught Error.\n' + jqXHR.responseText);
                }
            }
        });

});

function clear_messages(){
    $('.errors, .success, .non-field-errors').parent().remove();
}

function set_success(message){
    var i, html;

    if(message != ''){
        html = '<ul>';
        for (i in message){
            html += '<li class="success">'+message[i]+'</li>';
        }
        html += '</ul>';

        $('.message').html(html);
    }
}

function set_errors(obj_errors){
    var k, i, html1, html2;
    
    html1 = '<ul>';
    
    if('__all__' in obj_errors){
        for(i in obj_errors['__all__']){
            html1 += '<li class="non-field-errors">'+obj_errors['__all__'][i]+'</li>';
        }
        delete obj_errors.__all__
    }
    
    if(!$.isEmptyObject(obj_errors)){
        
        html1 += '<li>OCORREU UM ERRO NO FORMULARIO</li>';
        
        for(k in obj_errors){
            html2 = '<ul>';
            for(i in obj_errors[k]){
                html2+= '<li class="errors">'+obj_errors[k][i]+'</li>';
            }
            html2 += '</ul>';
            $('input[name="'+k+'"]').after(html2);
        }
    }
    
    html1 += '</ul>';
    
    $('.message').html(html1);
}

function clear_form(form) {
    $(':input', $(form)).each(function() {
      var type = this.type;
      var tag = this.tagName.toLowerCase(); // normalize case
      var name = this.name; // normalize case

      if (type == 'text' || type == 'password' || (type == 'hidden' && name != 'csrfmiddlewaretoken') || tag == 'textarea')
        this.value = "";
      else if (type == 'checkbox' || type == 'radio')
        this.checked = false;
      else if (tag == 'select')
        this.selectedIndex = -1;
    });
}

var timeoutId
function autocomplete(string_length, min_string_length, func)
{
    clearTimeout(timeoutId);
    timeoutId = setTimeout(function () {
        if(string_length >=  min_string_length || string_length == 0){
            func();
        }
     }, 400);
}
