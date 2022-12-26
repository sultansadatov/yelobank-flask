$(document).ready(function () {
    let header = $('.header');
    let headerTop = $('.header-top')
    let lastScrollTop = 0;
    let headerBottom = $('.header-bottom');
    let modal = $('.header-modal__close')
    let headerModal = $('.header-modal');
    let modalContent = $('#modalContent');

    $(modal).click(function (e) { 
        e.preventDefault();
        // console.log('sfsd');
        $(headerModal).toggleClass("active")
    });


    $(window).scroll(function (event) { 
        let currentPosition = $(this).scrollTop();
        if (currentPosition > 0){
            $(header).addClass('active');
            if (currentPosition > lastScrollTop){
                $(headerTop).height(0);
                $(headerBottom).addClass('opened')
                $(header).css('padding','0')
            } else {
                $(headerTop).height(35);
                $(headerBottom).removeClass('opened')
                $(header).css('padding','10')
            }
        }
        else{
            $(header).removeClass('active');
        }
        
        lastScrollTop = currentPosition;
    });

    const range = $('.range')
    let volPercentage = $(range).value * 100
    $(range).css({
        'background-color': `linear-gradient( to right, rgb(180, 170, 170) 0%, rgb(180, 170, 170) ${volPercentage}%, rgb(56, 50, 50) ${volPercentage}%, rgb(56, 50, 50) 100% )`
    })
});


