$(function() {

    $('#btn_salve').on('click', function(){
        $.post("/configuration/user/ajax/add/save", $('#form_user').serialize())
         .done(function(response){
             if(response.status == '1'){
                window.location = '/configuration/user/edit?id='+response.id;
             }
         }
        );
    });

});