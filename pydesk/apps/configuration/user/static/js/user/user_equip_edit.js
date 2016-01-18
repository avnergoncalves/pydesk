$(function() {

  $(".multiselect").multiselect({sortable: false, searchable: true});

  $('#btn_salve').on('click', function(){
        $.post("/configuration/user/equip/ajax/edit/save", $('#form').serialize())
         .done(function(response){
             //if(response.status == '1'){
                //window.location = '/configuration/user/equip/edit?id='+response.id;
             //}
         }
        );
    });

});