$(function () {

    //$('#search').keyup(function () {
    //    $.ajax({
    //        type: "POST",
    //        url: "/yarntail/search/",
    //        data: {
    //            'search_text': $('#search').val(),
    //            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
    //        },
    //        success: searchSuccess,
    //        dataType: 'html'
    //    });
    //
    //
    //});
    $('#search-button').click(function() {
        query = $('#search').val();
        spacelessQuery = query.replace(" ", "+");
        link = "/yarntail/search_results/" + spacelessQuery;
        window.location.replace(link);
});

});

function searchSuccess(data, textStatus, jqXHR) {
    $('#results').html(data);

}


