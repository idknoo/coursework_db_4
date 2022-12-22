$.ajax({
    method: 'GET',
    url: `/api/products/`,
    success: function (data_without_category) {
        console.log(data_without_category)

        $('.category-choice').on('click', function () {
            console.log(this.value)
            $.ajax({
                method: "GET",
                url: `/api/products/${this.value}/`,

                success: function (data_with_category) {
                    $('.product-container').children().children().empty()
                    for (const obj of data_with_category) {
                        console.log(obj.id)

                        let card = `<div class="card col-xl-3 col-lg-4 col-md-6 col-sm-12">
                                         <form method="POST" action="/order/single_product/">
                                             <img class="card-img-top" src=${obj.photo} alt="Card image cap">
                                             <div class="card-body">
                                                 <h5 class="card-title">${obj.product_name}</h5>
                                                 <h5 class="card-title card-category">${obj.category}</h5>
                                                 <p class="card-text">initial price: ${obj.initial_price}</p>
                                                 <p class="card-text">discount: ${obj.percent}</p>
                                                 <p class="card-text">final price: ${obj.final_price}</p>
                                                 <p class="card-text">stock: ${obj.stock}</p>
                                                 <p class="card-text">description: ${obj.description}</p>
                                                 <input value="${obj.id}">
                                                     <button type="submit" class="btn btn-primary">
                                                        view
                                                     </button>
                                             </div>
                                         </form>
                                    </div>`
                        $('.product-container').children().children().append(card)
                    }
                }
            })
        })

        for (const obj of data_without_category) {
            let card = `<div class="card col-xl-3 col-lg-4 col-md-6 col-sm-12">
                         <form method="POST" action="/order/single_product/">
                         <img class="card-img-top" src=${obj.photo} alt="Card image cap">
                         <div class="card-body">
                             <h5 class="card-title">${obj.product_name}</h5>
                             <h5 class="card-title card-category">${obj.category}</h5>
                             <p class="card-text">initial price: ${obj.initial_price}</p>
                             <p class="card-text">discount: ${obj.percent}</p>
                             <p class="card-text">final price: ${obj.final_price}</p>
                             <p class="card-text">stock: ${obj.stock}</p>
                             <p class="card-text">description: ${obj.description}</p>
                             <input value="${obj.id}" name="id" hidden>
                            <button type="submit" class="btn btn-primary">
                                                        view
                                                     </button>
                         </div>
                         </form>
                         </div>`
            $('.product-container').children().children().append(card)
        }
    },
    error: function () {
        console.log('error');
    }
})


// import {generate_card} from "./card";
// $('.product-container').children().children().append(generate_card(
//     product_name, category,
//     initial_price, final_price,
//     percent, stock,
//     description,
//     product_img
// ))
