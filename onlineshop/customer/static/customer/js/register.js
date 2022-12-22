$('#button').on('click', function () {
    console.log('button clicked');
    $.ajax({
        type: "POST",
        url: "/api/customers/register/",
        data: $('#form').serialize(),

        success: function (data) {
            console.log('Im in success!');
            console.log(data);
            location.href = data.link
        },
        error: function () {
            console.log('ERROR!!!');
            console.log(this.data);
        }
    })
})
