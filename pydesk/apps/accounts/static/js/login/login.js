$(function() {
    $('#btn_login').on('click', function(){
        $('#form_login').submit();
    });

    $('#id_username, #id_password').on('keydown', function(e){
        if (e.keyCode == 13) {
            $('#form_login').submit();
        }
    });
});