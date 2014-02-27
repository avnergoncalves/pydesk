$(function() {

	$("#grid_list_user").grid(
			{
				url : "/configuration/user/ajax/list",
				data:{
					find_user: $('#find_user'),
					status_user: $('#status_user')
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
									window.location.href = "/configuration/user/edit?id=" + res;
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
	
	$('#status_user').change(function(e){
		$('#grid_list_user').grid().reload({consultar:true});
	});
	
	$('#find_user').keyup(function(e){
		autocomplete(this.value.length, 3, function(){
			$('#grid_list_user').grid().reload({consultar:true});
		});
	});
	
	$('#btn_active').on('click', function(){
		if(confirm('Deseja ativar os itens selecionados ?')){
			$('#hdd_status').val('1');
			$.post("/configuration/user/ajax/toogle_status", $('#form_list_user').serialize())
			 .done(function(response){
				 if(response.status == '1'){
					$('#grid_list_user').grid().reload({consultar:true});
				 }
			 }
			);
		}
	});
	
	$('#btn_inative').on('click', function(){
		if(confirm('Deseja inativar os itens selecionados ?')){
			$('#hdd_status').val('0');
			$.post("/configuration/user/ajax/toogle_status", $('#form_list_user').serialize())
			 .done(function(response){
				 if(response.status == '1'){
					$('#grid_list_user').grid().reload({consultar:true});
				 }
			 }
			);
		}
	});

});