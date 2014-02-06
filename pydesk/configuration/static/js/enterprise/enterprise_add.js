$(function() {

	$('#btn_salve').on('click', function(){
		$.post("/configuration/enterprise/ajax/save", $('#form_enterprise').serialize())
		 .done(function(response){
			 if(response.status == '1'){
				 console.log('done'); 
			 }
		 }
		);
	});

});