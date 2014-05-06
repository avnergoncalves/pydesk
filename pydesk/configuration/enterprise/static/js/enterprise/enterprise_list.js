$(function() {

	$("#grid_list_enterprise").grid(
			{
				url : "/configuration/enterprise/ajax/list",
				data:{
					find_enterprise: $('#find_enterprise'),
					status_enterprise: $('#status_enterprise')
				},
				colluns : [
						{
							name : '<input type="checkbox" id="chk_all" />',
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
									window.location.href = "/enterprise/edit?id=" + res;
								}
							}
						},
						{
							name : "Ativo",
							order : false,
							th : {'width' : "5%"},
							icone : {'ativo': 'icone-preto ui-icon-check', 'inativo': 'icone-preto ui-icon-closethick'}
						} ]
			});
	
	$('#status_enterprise').change(function(e){
		$('#grid_list_enterprise').grid().reload({consultar:true});
	});
	
	$('#find_enterprise').keyup(function(e){
		autocomplete(this.value.length, 3, function(){
			$('#grid_list_enterprise').grid().reload({consultar:true});
		});
	});
	
	$('#btn_active').on('click', function(){
		if(confirm('Deseja ativar os itens selecionados ?')){
			$('#hdd_is_active').val('1');
			$.post("/configuration/enterprise/ajax/toogle_status", $('#form_list_enterprise').serialize())
			 .done(function(response){
				 if(response.status == '1'){
					$('#grid_list_enterprise').grid().reload({consultar:true});
				 }
			 }
			);
		}
	});
	
	$('#btn_inative').on('click', function(){
		if(confirm('Deseja inativar os itens selecionados ?')){
			$('#hdd_is_active').val('0');
			$.post("/configuration/enterprise/ajax/toogle_status", $('#form_list_enterprise').serialize())
			 .done(function(response){
				 if(response.status == '1'){
					$('#grid_list_enterprise').grid().reload({consultar:true});
				 }
			 }
			);
		}
	});

});