function initDatatables(csrftoken) {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true, // cuando se supera los 50.000 datos se pone en true
        searching: false, paging: false, info: false, ////// eliminar opciones
        bFilter: false, bInfo: false, ///// eliminar opciones
        "dom": 't', ///// eliminar opciones
        //"sDom": '<"top">rt<"bottom"flp><"clear">', ///// eliminar opciones
        "bJQueryUI": true,
        "sDom": 'lfrtip',
        "targets": 'no-sort',
        "bSort": false,
        "order": [],
        "bSortable": false, "aTargets": ["_all"],
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            data: {'action': 'searchdata'},
            dataSrc: "" // esto es para cuando se envía una variable en la colección
        },
        columns: [
            {"data": "icon"},
            {"data": "nameInCard"},
            {"data": "options"},
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'icon',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="' + data + '" class="img-thumbnail" >';
                }
            },
            {
                targets: [1],
                class: 'text',
                orderable: false,
                render: function (data, type, row) {
                    var enlace = '<p><b>Terminada en ' + row.number + '</b><br>' + row.nameInCard + '<br> Vencimiento 12/12 </p>';
                    return enlace;
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a rel="delete" class="btn btn-warning btn-xs"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}


$(function () {

    $('#data tbody').on('click', 'a[rel="delete"]', function () {
        var tr = $('#data').DataTable().cell($(this).closest('td, li')).index();
        var data = $('#data').DataTable().row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'delete');
        parameters.append('id', data.id);
        Swal.fire({
            title: '¿Estás seguro?',
            text: "¡No podrás revertir esta acción!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: '¡Si, bórralo!'
        }).then((result) => {
            if (result) {
                $.ajax({
                    url: window.location.pathname,
                    type: 'POST',
                    headers: {'X-CSRFToken': csrftoken},
                    data: parameters,
                    dataType: 'json',
                    processData: false,
                    contentType: false,
                }).done(function (data) {
                    if (!data.hasOwnProperty('error')) {
                        initDatatables(csrftoken);
                        Swal.fire(
                            '¡Eliminado!',
                            'Tarjeta eliminada con éxito.',
                        )
                        return false;
                    }
                    message_error(data.error);
                }).fail(function (jqXHR, textStatus, errorThrown) {
                    alert(textStatus + ': ' + errorThrown);
                }).always(function (data) {
                });
            }
        })
    })


    /*$('#data tbody').on('click', 'a[rel="delete"]', function () {
        var tr = $('#data').DataTable().cell($(this).closest('td, li')).index();
        var data = $('#data').DataTable().row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'delete');
        parameters.append('id', data.id);
        $.confirm({
            theme: 'material',
            title: 'Eliminar tarjeta',
            icon: 'fa fa-info',
            content: '¿Está seguro de eliminar esta tarjeta?',
            columnClass: 'small',
            typeAnimated: true,
            cancelButtonClass: 'btn-primary',
            draggable: true,
            dragWindowBorder: false,
            buttons: {
                info: {
                    text: "Si",
                    btnClass: 'btn-primary',
                    action: function () {
                        $.ajax({
                            url: window.location.pathname,
                            type: 'POST',
                            headers: {'X-CSRFToken': csrftoken},
                            data: parameters,
                            dataType: 'json',
                            processData: false,
                            contentType: false,
                        }).done(function (data) {
                            if (!data.hasOwnProperty('error')) {
                                initDatatables(csrftoken);
                                return false;
                            }
                            message_error(data.error);
                        }).fail(function (jqXHR, textStatus, errorThrown) {
                            alert(textStatus + ': ' + errorThrown);
                        }).always(function (data) {
                        });
                    }
                },
                danger: {
                    text: "No",
                    btnClass: 'btn-red',
                    action: function () {
                        //cancel();
                        // llamado de retorno o acción a ejecutar
                    }
                },
            }
        })


    })*/

    modal_title = $('.modal-title');

    $('.btnDebitAdd').on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Agregar tarjeta débito');
        modal_title.find('i').removeClass().addClass('fas fa-plus-circle');
        $('form')[0].reset(); // limpia el modal al salir de el
        $('#myModalCard').modal('show');
    });

    $('#myModalCard').on('shown.bs.modal', function () {
        $('form')[0].reset();
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
                $('#myModalCard').modal('hide');
                initDatatables(csrftoken);
                return false;
            }
            message_error(data.error);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {
        });
    });
})