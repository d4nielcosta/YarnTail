$(function () {

    $('#search').keyup(function () {
        $.ajax({
            type: "POST",
            url: "/yarntail/search/",
            data: {
                'search_text': $('#search').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'json'
        });
    });

});

function searchSuccess(data, textStatus, jqXHR) {
    $('#searchlist').empty();

    $('#searchlist').append('<option> -----Patterns----- </option>');
    for (pattern in data['patterns']) {
        $('#searchlist').append('<option><a href="' + data['patterns'][pattern]['url'] + '">' + data['patterns'][pattern]['title'] + '</a></option>');
    }
    $('#searchlist').append("<option> -----Users----- </option>");
    for (user in data['users']) {
    $('#searchlist').append('<option><a href="' + data['users'][user]['url'] + '">' + data['users'][user]['name'] + '</a></option>');
    }
}


