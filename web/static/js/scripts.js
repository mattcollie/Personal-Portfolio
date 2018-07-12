$(function(){
    var content = $(".content"),
        children = content.children(),
        _has_clicked_once = children.length <= 1;


    $('.content-body').click(function() {
        var me = this;
        _has_clicked_once = true;
        $('.click-notifier').removeClass('bounce-up-down').removeClass('bounce');
        if(children.length == 1)
            return;
        children.each(x => {
            if(children[x] == me) {
                var next = children[x + 1] || children[0];
                $(me).removeClass('fade-in');
                $(me).addClass('fade-out');
                setTimeout((function(next, me) { return _ => {
                    $(next).addClass('fade-in');
                    $(me).removeClass('fade-out');
                    next.style.display = 'flex';
                    me.style.display = 'none';
                }}(next, me)), 800);
            }
        });
    });


    setTimeout(function (){
        if(_has_clicked_once)
            return;
        $('.click-notifier').addClass('bounce-up-down').addClass('bounce');
    }, 10000);


})