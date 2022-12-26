/* Business Calculator */

$(document).on('input', '.range', function (e) {

    var t = $(this);
    tV = t.val();
    t.css("--val", tV);

    t.closest(".calculator-item").find(".range_result").val(tV);
    
    businessLoanCalculate($(this));

}) 

function businessLoanCalculate(item){
    let salary=parseFloat($('input[name=salary]').val());
    let period=parseFloat($('input[name=month]').val());
    let amount=parseFloat($('input[name=credit]').val());
    let p;
    console.log(period)
    if (period - 12 <= 0){
        percent = 0.14;
    }else if(parseInt(period / 12) == (period / 12)){
        percent = parseFloat(parseInt(period / 12) / 50) + 0.12;
    }else{
        percent = parseFloat(parseInt(period / 12) / 50) + 0.14;
    }   

    

    // console.log("-------" + percent + "-------")
    let p1 = Math.pow(1 + p, period);
    let p2 = (percent+1) * amount;
    let monthAmount = p2 / period;

    if (monthAmount / salary > 0.8){
        $('input[name=month]').attr('value', 48)
        $('input[name=month]').siblings('.range').attr({
            'value': 48,
            'style': '--min: 6; --max: 48; --val:48'
        })

        $('input[name=credit]').attr('value', 5175)
        $('input[name=credit]').siblings('.range').attr({
            'value': 5175,
            'style': '--min: 6; --max: 5175; --val:5175'
        })
        $('input[name=credit]').siblings('.range').attr('max', 5175);
        $('input[name=credit]').siblings('.range').css('width', '30%');

    }
    else{
        $('input[name=credit]').attr('value', 5175)
        $('input[name=credit]').siblings('.range').attr({
            'value': 5175,
            'style': `--min: 6; --max: 30000; --val:${$('input[name=credit]').val()}`
        })
        $('input[name=credit]').siblings('.range').attr('max', 30000);
        $('input[name=credit]').siblings('.range').css('width', '90%');
    }
    // else{
    //     $('input[name=month]').attr('value', 12)
    // }

    let arrMonthAmount = parseFloat(monthAmount).toFixed(2).split('.');
    // console.log(parseFloat(monthAmount), monthAmount, arrMonthAmount[0])

    $('input[name=pay_month_credit]').val(arrMonthAmount[0]);
    $('input[name=pay_month_percent]').val(percent);
    $('#my_month_pay').html(arrMonthAmount[0]+'.<span style="font-size:10px;">'+arrMonthAmount[1]+'</span><span> AZN</span>');

}

$(document).on('keyup', '.business_check', function (e) {
    var t = $(this);

    tV = t.val();
    r = t.siblings(".business_range")
    rMin = r.attr("min")
    rMax = r.attr("max");
    if (parseInt(tV) > parseInt(rMax)) t.val(rMax);
    if (parseInt(tV) < parseInt(rMin)) //t.val(rMin);
    if (tV.length < 1) t.val(rMin);
    tVnew = t.val();
    r.val(tVnew)
    r.css("--val", tVnew);
    if(tVnew>parseInt(rMin))
    {
        businessLoanCalculate();
    }

});


/* Business Calculator */