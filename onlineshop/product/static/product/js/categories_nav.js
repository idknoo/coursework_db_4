$.ajax({
    method: 'GET',
    url: '/api/products/categories/',
    success: function (categories) {
        console.log(categories)
        for (const cat of categories) {
            let cat_name = cat.category_name;
            let cat_link = `<button class="btn category-choice" value="${cat_name}"> ${cat_name}</button>`

            let cat_btn = $('#navbarSupportedContent').append(cat_link);
        }
        // cat_btn.on('click', function () {
        //     console.log('cat_link clicked')
        // })
    },
    error: function () {
        console.log('error in get data from category api!')
    }
})