"use strict"

const NAME_CART = "ttsdfsereerfsdfsdf2234ds67sdfs567nmvxsrfjrn34"
const btns = document.querySelectorAll(".btn__addToCart")
const btnClear = document.getElementById("clear-button")
const openCart = document.getElementById("open-cart")
const cartContent = document.getElementById("cart-content")
const cartNumber = document.getElementById("cart-number")
btns.forEach(btn => btn.addEventListener("click", event => {
    addToCart(event, "h5.card-title", "small.text-body-secondary")
    showItemCart()
    updateCartNumber()
}))
btnClear.addEventListener("click", () => {
    clearCart(NAME_CART)
    renderCart(cartContent)
    showItemCart()
    updateCartNumber()
})
showActiveLink("menu")
openCart.addEventListener("click", () => renderCart(cartContent))
showItemCart()
updateCartNumber()


// speicherung der Daten im local storage
function setCartData(cartData) {
    const jsonCartData = JSON.stringify(cartData)
    localStorage.setItem(NAME_CART, jsonCartData)
    return false
}


// daten aus local storage kriegen
function getCartData(NAME_CART) {
    const jsonCartData = localStorage.getItem(NAME_CART)
    return JSON.parse(jsonCartData)
}


// warenkorb ausleeren
function clearCart(NAME_CART) {
    localStorage.removeItem(NAME_CART)
}


// add to cart
function addToCart(event, titleSelector, priceSelector) {
    const btn = event.target
    btn.disabled = true
    const cartData = getCartData(NAME_CART) || {}
    const itemId = btn.dataset.id
    const title = btn.parentElement.querySelector(titleSelector).textContent
    const price = btn.parentElement.querySelector(priceSelector).textContent
    const img = btn.parentElement.parentElement.querySelector("img").src
    cartData[itemId] = { title, price, img }
    btn.disabled = setCartData(cartData)
}


// deleting only one product
function deleteItemCart(event) {
    const cartData = getCartData(NAME_CART)
    delete cartData[event.target.dataset.id]
    setCartData(cartData)
    showItemCart()
    updateCartNumber()
    renderCart(cartContent)
}


// is the product already in the cart?
function showItemCart() {
    const cartData = getCartData(NAME_CART)
    btns.forEach(btn => {
        if (cartData && cartData.hasOwnProperty(btn.dataset.id)) {
            btn.textContent = "Added to cart"
            btn.className = "btn btn-success btn__addToCart"
        } else {
            btn.textContent = "Add to cart"
            btn.className = "btn btn-warning btn__addToCart"
        }
    })
}


//updating cart number
function updateCartNumber() {
    const cartData = getCartData(NAME_CART)
    cartNumber.textContent = cartData ? Object.keys(cartData).length : ""
}


function showActiveLink(menu) {
    try {
        const url = document.location.href;
        const links = document.getElementById(menu).querySelectorAll("a")
        for (const link of links) {
            if (link.href === url) {
                link.classList.add("active")
            }
        }
    } catch (e) {
        console.log(e)
    }

}

// warenkorb zeichnen
function renderCart(cart) {
    const cartData = getCartData(NAME_CART)
    let price = 0
    let content = ""
    if (cartData === null || Object.keys(cartData).length === 0) {
        content = "<h1 class='text-center'>Cart is empty</h1>"
    } else {
        content = `<table class="table"><tbody>`
        for (const productId in cartData) {
            /* const product = cartData[productId]
            content += "<tr>"
            for (const prop in product) {
                content += `<td>${product[prop]}</td>`
            }
            content += `<td><button class="btn btn-danger" data-id="${productId}" onclick="deleteItemCart(event)">Delete</button></td> </tr>`
            price += +product["price"] */
            const product = cartData[productId]
            price += +product["price"]
            content += `
            <tr> 
                <td>${product.title}</td>
                <td>${product.price}</td>
                <td class="cart-img"><img src="${product.img}" alt="${product.title}" style="width: 100%;"></td>
                <td><button class="btn btn-danger" data-id="${productId}" onclick="deleteItemCart(event)">Delete</button></td>
            </tr>`
        }
        content += "</tboby></table>"
        content += `<div class="text-center">Total price: $${price}</div>`
    }
    cart.innerHTML = content
}
