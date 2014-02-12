$(function() {

	$("#grid_list_enterprise").grid(
			{
				url : "/configuration/enterprise/ajax/list",
				colluns : [
						{
							name : "Razão Social",
							th : {'width' : "40%"},
							td : {'align' : "left"}
						},
						{
							name : "Nome Fantasia",
							th : {'width' : "40%"},
							td : {'align' : "left"}
						},
						{
							name : "CNPJ",
							th : {'width' : "10%"}
						},
						{
							name : "Editar",
							order : false,
							th : {'width' : "5%"},
							acoes : {
								"editar" : function(res, row_id) {
									window.location.href = site_url
											+ "/sinc/usuario/editar/" + res;
								}
							}
						},
						{
							name : "Ativar/Inativar",
							order : false,
							th : {'width' : "5%"},
							acoes : {
								"ativar" : function(res, row_id) {
									ativar(res);
								},
								"inativar" : function(res, row_id) {
									inativar(res);
								}
							}
						} ]
			});

});