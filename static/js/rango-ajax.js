$(document).ready(function() {

$('#likes').click(function(){
    var name;
    name = $(this).attr("data-name");

    // var _href = $('a.replaceValue').attr('href');

    $.get('/getgroupname/', {group_name: name}, function(data){
        $('.replaceValue').each(function() {
            var $this = $(this);
            var _href = $this.attr("href");



               // $('#like_count').html(data);
               // $("a#like_count").attr('href', '/'+ data + '/' + _href);
               $($this).html(data + _href);
               $($this).attr('href', '/details/' + data + _href);
               });
           });
});

});