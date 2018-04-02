/**
 * Created by wangkai on 2018/3/31.
 */

$(function () {
   $("#codePic1").on("click touchend", function () {
        $.ajax({
        type: 'GET',
        url: '/codePicCreator',
        // dataType: 'json',
        timeout: 300,
        // context: $('body'),
        success: function (data) {
            // $(this).attr({'src':"data:;base64,{{ base64.b64encode("+data+") }}"});
            $("#codePic1").attr({"src":"/codePicCreator"});
        },
        error: function (xhr, type) {
            console.log('Ajax error! greenhouse get Log')
        }
    });
   })
});