$(document).ready(function() {

$('#likes').change(function(){
    var name;
    var token;
    name = $(this).attr("data-name");
    token = $(this).attr("data-access-token");
    token = '?access_token=' + token;

    // $.get('/getgroupname/', {group_name: name }, function(data){
    $.get('/getgroupname/', {group_name: name, access_token: token }, function(data){
        $('.replaceValue').each(function() {
            var $this = $(this);
            var _href = $this.attr("href");

               $($this).attr('href', '/details/' + data + _href + token);
               });
           });
});

});