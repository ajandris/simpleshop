/**
 *
 * Shopping cart functions and structure
 */
const cart = {
    discount: {             // available discount
        type: 'percentage', // or 'fixed'
        value: 10, // 10% off or £10 off
        code: 'WELCOME10',
        used: 'no', // changes to yes when used
    },
    products: [],

    addProduct(sku, title, qty, unitPrice){
        product = {
            sku: sku,
            title: title,
            qty: qty,
            unitPrice: unitPrice
        }
        this.products.push(product);
    },

    removeProduct(sku){
        for (let i = 0; i < this.products.length; i++){
            if (this.products[i].sku.upper === sku){
                this.products.splice(i, 1);
            }
        }
    },

    updateProductQty(sku, qty){

    },

    incerementProductQty(sku, incrementBy){

    },

    decreseProductQty(sku, decreseBy){

    },


}


function main(cart){

    const cart_no = sessionStorage.getItem('cart_number');
    console.log('Cart Number: ', cart_no);

    // cart.addProduct('sku001', 'Title 1', 2, '16.78');
    // cart.addProduct('sku002', 'Title 2', 2, '26.78');
    // cart.addProduct('sku003', 'Title 3', 2, '36.78');
    // localStorage.setItem('cart', JSON.stringify(cart))
    // let savedCart = JSON.parse(localStorage.getItem('cart'));
    // console.log(savedCart);
    //
    // cart.removeProduct('sku002');
    // localStorage.setItem('cart', JSON.stringify(cart))
    // savedCart = JSON.parse(localStorage.getItem('cart'));
    // console.log(savedCart);


    // Event Listeners
    document.addEventListener('DOMContentLoaded', ()=>{
       // adds other listeners only when DOM is loaded


    })
}
main(cart);