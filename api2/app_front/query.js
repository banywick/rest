


let button = document.querySelector('#button')
button.addEventListener('click', fn)
let main = document.querySelector('#main')
function  fn(){
    main.innerHTML=''
    fetch('https://santrok.pythonanywhere.com/barter/api/v1/show_product/')
        .then(resp=> resp.json())
        .then(data=>{
            console.log(data);
            data.map(item=>{
                main.innerHTML+=`<div class="card">
                            <p>${item.name}</p>
                            <p>${item.price}</p>
                            <p>${item.category}</p>

                             </div>`
            })


        })

    setInterval(()=>{
             main.innerHTML=''
        fetch('https://santrok.pythonanywhere.com/barter/api/v1/show_product/')
        .then(resp=> resp.json())
        .then(data=> {
            console.log(data);
            data.map(item => {
                main.innerHTML += `<div class="card">
                            <p>${item.name}</p>
                            <p>${item.price}</p>
                            <p>${item.category}</p>
                             </div>`
        })
        })
    }, 1000)

}
