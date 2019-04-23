$(document).ready(function() {

$('#likes').click(function(){
    var catid;
    var _href = $("a.directions-link").attr("href");
    catid = $(this).attr("data-catid");
     $.get('/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $("a#like_count").attr('href', '/'+ data + '/' + _href);
           });
});

});