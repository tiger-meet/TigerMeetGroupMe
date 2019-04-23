$(document).ready(function() {

$('#likes').click(function(){
    var catid;
    catid = 2;
     $.get('/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
           });
});

});