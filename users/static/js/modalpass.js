$(function () {
    modal_title = $('.modal-title');

    $('.btnChangePass').on('click', function () {
        $('input[name="action"]').val('change_pass');
        modal_title.find('span').html('Cambiar contraseña');
        modal_title.find('i').removeClass().addClass('fas fa-exclamation-triangle');
        $('#ModalChangePass').modal('show');
    });


    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: parameters,
            dataType: 'json',
            processData: false,
            contentType: false,
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: 'La contraseña ha sido cambiada',
                    showConfirmButton: false,
                    timer: 1500
                })
                $('#ModalChangePass').modal('hide');
                return false;
            }
            message_error(data.error);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {
        });
    });
})

