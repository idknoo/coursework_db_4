$('#button').on('click', function () {
    console.log('button clicked');
    $.ajax({
        type: "POST",
        url: "/api/customers/forgetpassword/",
        data: $('#form').serialize(),

        success: function (data) {
            console.log('Im in success!');
            console.log(data);
            location.href = data.link
        },
        error: function (data) {
            console.log('ERROR!!!');
            location.href = this.url

        }
    })
})
