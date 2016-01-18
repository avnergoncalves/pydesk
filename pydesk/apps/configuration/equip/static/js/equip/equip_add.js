$(function() {

	$('#btn_save').on('click', function(){
		$.post("/configuration/equip/ajax/save", $('#form_equip').serialize())
		 .done(function(response){
			 if(response.status == '1'){
				var id = $('#id_id').val();
				if(id == ''){
					clear_form('#form_equip');
				}
			 }
		 }
		);
	});
	
	$('#btn_back').on('click', function(){
		window.location.href = '/configuration/equip/list#grid=1';
	});

});