$(function(){
    $.ajax({
        url: 'test.py',
        type: 'post',
        data: 'massage'
    }).done(function(data){
        console.log(data);
    }).fail(function(){
        console.log('failed');
    });
});