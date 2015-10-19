$(function() {

    $('#btn_salve').on('click', function(){
        $.post("/configuration/user/ajax/edit/save", $('#form_user').serialize())
         .done(function(response){
             if(response.status == '1'){

             }
         }
        );
    });

});