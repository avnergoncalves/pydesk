$(function() {

	$('#btn_save').on('click', function(){
		$.post("/configuration/project/ajax/save", $('#form_project').serialize())
		 .done(function(response){
			 if(response.status == '1'){
				var id = $('#id_id').val();
				if(id == ''){
					clear_form('#form_project');
				}
			 }
		 }
		);
	});
	
	$('#btn_back').on('click', function(){
		window.location.href = '/configuration/project/list#grid=1';
	});

});