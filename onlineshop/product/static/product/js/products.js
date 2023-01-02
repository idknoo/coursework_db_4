$.ajax({
    method: 'GET',
    url: `/api/products/`,
    success: function (data) {
        console.log(data)
        for (const obj of data) {
            let card = `<div class="card col-xl-3 col-lg-4 col-md-6 col-sm-12">
                         <form method="POST" action="/order/single_product/">
                         <img class="card-img-top" src=${obj.photo} alt="Card image cap">
                         <div class="card-body">
                             <h5 class="card-title">${obj.animal_name}</h5>
                             <p class="card-text">Specie: ${obj.specie}</p>
                             <p class="card-text">Age: ${obj.age}</p>
                             <p class="card-text">Gender: ${obj.gender}</p>
                             <p class="card-text">Health: ${obj.health}</p>
                             
                             <input value="${obj.id}" name="id" hidden>
                            <button type="submit" class="btn btn-primary">
                                                        view
                                                     </button>
                         </div>
                         </form>
                         </div>`
            if (obj.is_given != true){
                $('.product-container').children().children().append(card)
            }
        }
    },
    error: function () {
        console.log('error');
    }
})

