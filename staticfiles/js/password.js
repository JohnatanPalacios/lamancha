$(function (){
    var mayus = new RegExp("^(?=.*[A-Z].*[A-Z])");
    var special = new RegExp("^(?=.*[!@#$%&*].*[!@#$%&*])");
    var numbers = new RegExp("^(?=.*[0-9].*[0-9])");
    var lower = new RegExp("^(?=.*[a-z].*[a-z].*[a-z])");
    var len = new RegExp("^(?=.{8,})");

    var regExp = [mayus, special, numbers, lower, len];

    $("#id_password1").on("keyup", function (){
        var pass = $("#id_password1").val();
        check = 0;

        for(let i=0; i<regExp.length; i++){
            if(regExp[i].test(pass)){
                check++;
            }
        }

        if(check >= 0 && check <= 2){
            $("#feedback_password1").text("Nivel bajo").css("color", "red");
        }else if(check >= 3 && check <= 4){
            $("#feedback_password1").text("Nivel medio").css("color", "orange");
        }else if(check == 5){
            $("#feedback_password1").text("Nivel alto").css("color", "green");
        }
    });
    $("#id_password2").on("keyup", function (){
        var pass1 = $("#id_password1").val()
        var pass2 = $("#id_password2").val()
        $("#feedback_password2").text("");
        if(pass1 != pass2){
            $("#feedback_password2").text("Las contraseñas deben ser iguales").css("color", "red");
        }
    })
});
