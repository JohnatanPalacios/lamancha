$(function () {
    const birthdayField = document.querySelector("#id_birthday")
    const birthdayArea = document.querySelector("#feedback_birthday")

    $("#id_birthday").on("keyup", function () {
        var date = $("#id_birthday").val();
        var date = ((moment(date, "YYYYMMDD").fromNow(true)).split(" "))[0];

        birthdayField.classList.remove("is-invalid");
        birthdayArea.style.display="none";

        //$("#feedback_birthday").text("");
        if (date > 80 || date < 18) {
            //$("#feedback_birthday").text("Edad no permitida").css("color", "red");
            birthdayField.classList.add("is-invalid");
            birthdayArea.style.display="block";
            birthdayArea.innerHTML='<p>Edad no permitida</p>';
        }
    })
})