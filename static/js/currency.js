$(document).ready(function () {
    let result_currency = $('.result_currency');
    let input_currency = $('.input_currency');
    let from_currency = $('select[name="from"]').val();
    let to_currency = $('select[name="to"]').val();

    

    $(input_currency).keyup(function (e) { 

        $('select').on('change', function() {
            from_currency = $('select[name="from"]').val();
            to_currency = $('select[name="to"]').val();
            e.preventDefault();
            if (e.target.value == ""){
                $(result_currency).text("Alıram");
            }else{
                fetch(`https://api.exchangerate.host/latest?base=${to_currency}&symbols=${from_currency}`)
                .then(res => res.json())
                    .then(data => {
                        $(result_currency).text((input_currency.val() / data.rates[from_currency]).toFixed(2));
                    })
                .catch(err => alert("Error: " + err))
            }
          });
        e.preventDefault();
        if (e.target.value == ""){
            $(result_currency).text("Alıram");
        }else{
            fetch(`https://api.exchangerate.host/latest?base=${to_currency}&symbols=${from_currency}`)
            .then(res => res.json())
                .then(data => {
                    $(result_currency).text((input_currency.val() / data.rates[from_currency]).toFixed(2));
                })
            .catch(err => alert("Error: " + err))
        }
    });
});