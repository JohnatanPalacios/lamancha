function initDatatables(csrftoken) {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true, // cuando se supera los 50.000 datos se pone en true
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            data: { 'action': 'searchdata' },
            dataSrc: "" // esto es para cuando se envía una variable en la colección
        },
        columns: [
            {"data": "id"},
            {"data": "title"},
            {"data": "author"},
            {"data": "price"},
            {"data": "options"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/books/book/update/' + row.id + '/" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/books/book/delete/' + row.id + '/" class="btn btn-warning btn-xs"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
};