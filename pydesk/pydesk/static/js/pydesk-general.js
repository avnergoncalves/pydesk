$(function() {

	$(function () {

		$.ajaxSetup({
			success:function(response){
				clear_errors();
				
				if(response.status == '0'){
					set_errors(response.errors);
				}
			},
				
			error: function(jqXHR, exception) {

				console.log(jqXHR.status);

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

});

function clear_errors(){
	$('.errorlist, .non-field-errors').remove();
}

function set_errors(obj_errors){
	var k, i, html1, html2;
	
	html1 = '<ul class="non-field-errors">';
	
	if('__all__' in obj_errors){
		for(i in obj_errors['__all__']){
			html1 += '<li>'+obj_errors['__all__'][i]+'</li>';
		}
		delete obj_errors.__all__
	}
	
	if(!$.isEmptyObject(obj_errors)){
		
		html1 += '<li>OCORREU UM ERRO NO FORMULARIO</li>';
		
		for(k in obj_errors){
			html2 = '<ul class="errorlist">';
			for(i in obj_errors[k]){
				html2+= '<li>'+obj_errors[k][i]+'</li>';
			}
			html2 += '</ul>';
			$('input[name="'+k+'"]').after(html2);
		}
	}
	
	html1 += '</ul>';
	
	$('.message').html(html1);
}
