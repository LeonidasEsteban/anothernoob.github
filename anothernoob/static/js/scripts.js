var login_timeout;

//login box
function close_login_box() {
    var $login_button = $('#login-button'),
        $login_box = $('#login-box'),
        $nav = $('nav');
    if($nav.hasClass('open')) {
        $nav.height($nav.height()-$login_box.height()-25);
    }
    $login_button.removeAttr('style');
    $login_button.removeClass('open');
    
    window.clearInterval(login_timeout);
}
function open_login_box() {
    var $login_button = $('#login-button'),
        login_button_height,
        $login_box = $('#login-box'),
        login_box_height,
        $nav = $('nav');
    
    if(!$login_button.hasClass('open')) {
        login_button_height = $login_button.height();
        login_box_height = $login_box.height();
        $login_button.height(login_button_height + login_box_height + 40);
        $login_button.addClass('open');
        if($nav.hasClass('open')) {
            $nav.height($nav.height()+$login_box.height()+25);
        }
    } else {
        close_login_box();
    }
}
function navStyle() {
    var offset = $(window).scrollTop();
    close_login_box();
    close_mobile_menu();
    
    if(offset > 5) {
        $('nav').addClass('float');
    } else {
        $('nav').removeClass('float');
    }
}
function open_mobile_menu() {
    var $menu = $('nav'),
        count = $menu.children('ul').children('.mobile-item').length;

    if(!$menu.hasClass('open')) {
        $menu.addClass('open');
        $menu.height(count * 42);
    } else {
        close_mobile_menu();
    }
}
function close_mobile_menu() {
    var $menu = $('nav');

    close_login_box();

    $menu.removeClass('open');
    $menu.height(42);
}

$(window).on('scroll', navStyle);
$('#login-button').on('click', open_login_box);
$('#mobile_menu').on('click', open_mobile_menu);