$(document).ready(function () {
    $(document).on('click', '#search-button', function(e){
        search_value = $('#search-input').val();
        call_search_filter(search_value);
     });
     
     $(document).on('keypress', "#search-input", function(e){
         const c = (e.keyCode ? e.keyCode : e.which);
         if(c == 13) {
            search_value = $('#search-input').val();
            call_search_filter(search_value);
         }
     });
});

function call_search_filter(search_text) {
    const url = "/videos/filter_submit";
    const data = {
        'search_query' : search_text
    }
    $.ajax({
        url: url,
        data: data,
        success: update_search_filter,
        type: "POST"
    });
}

function update_search_filter(data) {
    try {
        if (!data.success) {
            if (data.error) {
                alert(data.error)
            }
        } else {
            $('#video_details').html(data.video_details_view);
            $('#page_numbers').html(data.page_number_view);
            if (data.search_value) {
                $('#heading_search').html("YouTube API videos page - search query: " + data.search_value + ", " + data.total_results + " total results")
            } else{
                $('#heading_search').html("YouTube API videos page - " + data.total_results + " total results")
            }
        }
    } catch (e) {
        
    }
}
