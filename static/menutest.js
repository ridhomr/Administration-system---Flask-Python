// Add active class to the current button (highlight it)
$('li > a').click(function() {
    $('li').removeClass();
    $(this).parent().addClass('active');
});