

$(document).on('click', '#block', function(e){
    var $type = $(this).data("block-source");
    if($type == "all"){
      $('.blocks').fadeOut(0);
      $('.blocks').fadeIn(1000);
    

    }else{
      $('.blocks').hide();
    
      $('#'+$type + ".blocks").fadeIn(1000);

    }
    
  })

  $(document).ready(function(){
    let btns = $('.question')

    // btns.each(btn => {
    //   btn.click(function(e){
    //     console.log(e.target);
    //   })
    // });
    // jQuery.each(btns, function(btn){
    //   btn.on('click', function(){
    //     btn.sibling('div').css("display", "block")
    //   })
    // })

    for(var i=0; i< btns.length; i++) {
      $(btns[i]).on('click', function(e){
        $(this).next().toggle("active")
      })
    }

    // console.log(btns);
  })
