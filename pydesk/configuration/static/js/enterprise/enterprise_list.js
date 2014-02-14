$(function() {

	$("#grid_list_enterprise").grid(
			{
				url : "/configuration/enterprise/ajax/list",
				data:{
					rasao_social: $('#filter_enterprise'),
					nome_fantasia: $('#filter_enterprise')
				},
				colluns : [
						{
							name : '<input type="checkbox" />',
							th : {'width' : "5%"},
							td : {'align' : "left"},
							order : false,
							acoes : {
								"checkbox" : function(res, row_id) {
									console.log('click');
								},
							}
						},
						{
							name : "Razão Social",
							th : {'width' : "35%"},
							td : {'align' : "left"}
						},
						{
							name : "Nome Fantasia",
							th : {'width' : "30%"},
							td : {'align' : "left"}
						},
						{
							name : "CNPJ",
							th : {'width' : "20%"}
						},
						{
							name : "Editar",
							order : false,
							th : {'width' : "5%"},
							acoes : {
								"editar" : function(res, row_id) {
									window.location.href = "/configuration/enterprise/edit?id=" + res;
								}
							}
						},
						{
							name : "Status",
							order : false,
							th : {'width' : "5%"},
							icone : {'ativo': 'icone-preto ui-icon-check', 'inativo': 'icone-preto ui-icon-closethick'}
						} ]
			});
	
	$('#filter_enterprise').keyup(function(e){
		if(e.keyCode == 13){
			$('#grid_list_enterprise').grid().reload({consultar:true});
		}
	});
	
	$('#btn_active').on('click', function(){
		
		$('#ipt_status').val('A');
		
		$.post("/configuration/enterprise/ajax/toogle_status", $('#form_list_enterprise').serialize())
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

});