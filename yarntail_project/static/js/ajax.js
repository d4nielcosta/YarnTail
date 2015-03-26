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
        //alert(data);
    });

    //$('#search-button').click(function () {//search button works without this, remove after a day or two
    //    query = $('#search').val();
    //    spacelessQuery = query.split(" ").join("+");
    //    link = "/yarntail/search_results/" + spacelessQuery;
    //    window.location.replace(link);
    //});

});

function searchSuccess(data, textStatus, jqXHR) {
    $('#results').empty();
    console.log("asfghj");
    console.log(data);

    for (pattern in data['patterns']) {
        $('#results').append('<li><a href="' + data['patterns'][pattern]['url'] + '">' + data['patterns'][pattern]['title'] + '</a></li>');
    }
    for (user in data['users']) {
    $('#results').append('<li><a href="' + data['users'][user]['url'] + '">' + data['users'][user]['name'] + '</a></li>');
    }
}


