$(function() {

	$('#btn_save').on('click', function(){
		$.post("/enterprise/ajax/save", $('#form_enterprise').serialize())
		 .done(function(response){
			 if(response.status == '1'){
				var id = $('#id_id').val();
				if(id == ''){
					clear_form('#form_enterprise');
				}
			 }
		 }
		);
	});
	
	$('#btn_back').on('click', function(){
		window.location.href = '/enterprise/list#grid=1';
	});
	
	$("#id_cnpj").mask("99.999.999/9999-99");

});