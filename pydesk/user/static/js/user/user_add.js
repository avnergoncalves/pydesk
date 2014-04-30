$(function() {

	$('#btn_salve').on('click', function(){
		$.post("/user/ajax/save", $('#form_user').serialize())
		 .done(function(response){
			 if(response.status == '1'){
				var id = $('#id_id').val();
				if(id == ''){
					clear_form('#form_user');
				}
			 }
		 }
		);
	});
	
	
	$(".chosen-select").chosen({width: "100%"});
	
});