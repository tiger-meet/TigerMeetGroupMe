$(document).ready(function() {

// $('#likes').change(function(){
    var name;
    var token;
    name = $('#likes').attr("data-name");
    token = $('#likes').attr("data-access-token");
    token = '?access_token=' + token;

    // $.get('/getgroupname/', {group_name: name }, function(data){
    $.get('/getgroupname/', {group_name: name, access_token: token }, function(data){
        $('.replaceValue').each(function() {
            var $this = $(this);
            var _href = $this.attr("href");

               $($this).attr('href', '/details/' + data + _href + token);
               });
           // });
});

    $.get('/getgroupname/', {group_name: name, access_token: token }, function(data){
        $('.MyReplaceValue').each(function() {
            var $this = $(this);
            var _href = $this.attr("href");

               $($this).attr('href', '/details/' + _href + token);
               });
           // });
});

});