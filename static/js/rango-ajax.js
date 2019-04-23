$(document).ready(function() {

$('#likes').click(function(){
    var name;
    var token;
    name = $(this).attr("data-name");
    token = $(this).attr("data-access-token");
    token = '?access_token=' + token;

    // var _href = $('a.replaceValue').attr('href');

    $.get('/getgroupname/', {group_name: name, access_token: }, function(data){
        $('.replaceValue').each(function() {
            var $this = $(this);
            var _href = $this.attr("href");



               // $('#like_count').html(data);
               // $("a#like_count").attr('href', '/'+ data + '/' + _href);
               $($this).attr('href', '/details/' + data + _href + token);
               });
           });
});

});