/**
 * Created by wangkai on 2018/4/1.
 */

$(function () {
    $("[id='deleteBtn']").on("click touchend", function () {
        $.post("imgDelete",
            {
                imagNmae: $(this).name
            },
            function (data, status) {
                alert("数据：" + $(this).name);
                $(this).parent().remove();
            });
    })
});