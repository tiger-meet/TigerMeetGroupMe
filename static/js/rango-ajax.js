$(document).ready(function() {

$('#likes').click(function(){
    var catid;
    catid = 2;
     $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
           });
});

});