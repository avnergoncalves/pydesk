$(function() {

	$('#btn_salve').on('click', function(){
		$.post("/configuration/enterprise/ajax/save", $('#form_enterprise').serialize())
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

	$("#id_cnpj").mask("99.999.999/9999-99");

});