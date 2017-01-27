
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();

    $('#comment-popover-button').popover({
        html:true,
        content: function(){
            $('#comment-popover-content textarea').outerWidth("100%");
            return $('#comment-popover-content').html();
        }});
});

