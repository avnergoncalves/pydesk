$(function() {

	$("#grid_list_equip").grid(
			{
				url : "/configuration/equip/ajax/list",
				data:{
					find: $('#find'),
					status: $('#status')
				},
				colluns : [
						{
							name : '<input type="checkbox" id="chk_all" />',
							th : {'width' : "5%"},
							td : {'align' : "left"},
							order : false,
							acoes : {
								"checkbox" : function(res, row_id) {
									//console.log('click');
								},
							}
						},
						{
							name : "Descrição",
							th : {'width' : "35%"},
							td : {'align' : "left"}
						},
						{
							name : "Editar",
							order : false,
							th : {'width' : "5%"},
							acoes : {
								"editar" : function(res, row_id) {
									window.location.href = "/configuration/equip/edit?id=" + res;
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
	
	$('#status').change(function(e){
		$('#grid_list_equip').grid().reload({consultar:true});
	});
	
	$('#find').keyup(function(e){
		autocomplete(this.value.length, 3, function(){
			$('#grid_list_equip').grid().reload({consultar:true});
		});
	});
	
	$('#btn_active').on('click', function(){
		if(confirm('Deseja ativar os itens selecionados ?')){
			$('#hdd_is_active').val('1');
			$.post("/configuration/equip/ajax/toogle_status", $('#form_list_equip').serialize())
			 .done(function(response){
				 if(response.status == '1'){
					$('#grid_list_equip').grid().reload({consultar:true});
				 }
			 }
			);
		}
	});
	
	$('#btn_inative').on('click', function(){
		if(confirm('Deseja inativar os itens selecionados ?')){
			$('#hdd_is_active').val('0');
			$.post("/configuration/equip/ajax/toogle_status", $('#form_list_equip').serialize())
			 .done(function(response){
				 if(response.status == '1'){
					$('#grid_list_equip').grid().reload({consultar:true});
				 }
			 }
			);
		}
	});

});