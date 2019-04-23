$(document).ready(function() {

$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");

    // var _href = $('a.replaceValue').attr('href');

    $.get('/like_category/', {category_id: catid}, function(data){
        $('.replaceValue').each(function() {
            var $this = $(this);
            var _href = $this.attr("href");



               // $('#like_count').html(data);
               // $("a#like_count").attr('href', '/'+ data + '/' + _href);
               $('.replaceValue').html(data);
               $('.replaceValue').attr('href', '/'+ data + '/' + _href);
               });
           });
});

});