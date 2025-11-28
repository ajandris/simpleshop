/**
 *
 * Shopping cart functions and structure
 */

function cart() {

    const VAT_RATE = 20;

    function updateShippingOptions(subTotal) {
        const select = document.getElementById('shipping');
        const setOptions = document.getElementsByClassName('ship-data');
        for (const sh of setOptions) {
            let discountThreshold = parseFloat(sh.dataset.shipThreshold);
            if (discountThreshold <= subTotal) {
                // change shipping option price
                let shipSelectOption =
                    document.getElementById('shipping-' + sh.dataset.shipCode);
                shipSelectOption.value = sh.dataset.shipDiscountedPrice;
                shipSelectOption.textContent = sh.dataset.shipText + ' - £' + sh.dataset.shipDiscountedPrice;
            } else {
                let shipSelectOption =
                    document.getElementById('shipping-' + sh.dataset.shipCode);
                shipSelectOption.value = sh.dataset.shipPrice;
                shipSelectOption.textContent = sh.dataset.shipText + ' - £' + sh.dataset.shipPrice;
            }
        }
    }


    function recalculate() {
        let items = document.getElementsByClassName('cart-item');
        let sku = "";
        let price = 0.00;
        let qty = 1;
        let line = 0.00
        let subTotal = 0
        for (let i = 0; i < items.length; i++) {
            sku = items[i].dataset.sku;
            price = items[i].dataset.price;
            qty = parseInt(document.getElementById(sku + '-qty').value, 10);
            line = price * qty;
            subTotal += line;
            document.getElementById(sku + '-line').textContent = line.toFixed(2);
        }
        document.getElementById("subtotal").textContent = subTotal.toFixed(2);
        updateShippingOptions(subTotal);

        let discountObj = document.getElementById('coupon-data');
        let discount = 0.00;
        if (discountObj) {
            if (discountObj.dataset.couponType === "percent") {
                discount = subTotal * parseFloat(discountObj.dataset.couponValue) / 100;
            }
            if (discountObj.dataset.couponType === "amount") {
                discount = parseFloat(discountObj.dataset.couponValue);
            }
            document.getElementById('discount').textContent = discount.toFixed(2);
        }

        let totalAmount = subTotal - discount +
            parseFloat(document.getElementById('shipping').value);
        document.getElementById('total').textContent = totalAmount.toFixed(2);

        let vatValue = totalAmount * VAT_RATE / (100 + VAT_RATE);
        document.getElementById('vat').textContent = vatValue.toFixed(2);
    }

    function decrQty(sku) {
        // decrement (minus) by one
        let qtyField = document.getElementById(sku + '-qty');
        let currQty = parseInt(qtyField.value, 10);
        let newQty = currQty - 1;
        if (newQty >= 1) {
            qtyField.value = newQty.toString();
        }
        recalculate();
    }

    function incrQty(sku) {
        // decrement (minus) by one
        let qtyField = document.getElementById(sku + '-qty');
        let currQty = parseInt(qtyField.value, 10);
        let newQty = currQty + 1;
        qtyField.value = newQty.toString();
        recalculate();
    }

    function setQty(sku) {
        recalculate()
    }


    function removeTechnicalFields(frm) {
        let techFields = document.getElementsByClassName('tech-field');
        for (let fld of techFields) {
            frm.removeChild(fld);
        }
    }

    function updateCart() {
        /**
         * submit to database cart state
         */
        let frm = document.getElementById('form-template');
        frm.method = 'POST';
        frm.action = document.getElementById('update-cart').value;

        let items = document.getElementsByClassName('item-qty');
        for (let item of items) {
            let inputField = document.createElement('input');
            inputField.type = 'hidden';
            let id = item.id;
            inputField.name = 'sku-' + id.split('-')[0];
            inputField.value = item.value;
            frm.appendChild(inputField);
        }

        let ship = document.getElementById('shipping');
        let inputField = document.createElement('input');
        inputField.type = 'hidden';
        inputField.name = 'shipping';
        inputField.value = ship.options[ship.selectedIndex].id.split('-')[1];
        frm.appendChild(inputField);

        removeTechnicalFields(frm);
        frm.submit();
    }

    function checkout() {
        /**
         * @type {HTMLElement}
         */
        let frm = document.getElementById('form-template');
        frm.method = 'POST';
        frm.action = document.getElementById('checkout').value;

        let items = document.getElementsByClassName('item-qty');
        for (let item of items) {
            let inputField = document.createElement('input');
            inputField.type = 'hidden';
            let id = item.id;
            inputField.name = 'sku-' + id.split('-')[0];
            inputField.value = item.value;
            frm.appendChild(inputField);
        }

        let ship = document.getElementById('shipping');
        let inputField = document.createElement('input');
        inputField.type = 'hidden';
        inputField.name = 'shipping';
        inputField.value = ship.options[ship.selectedIndex].id.split('-')[1];
        frm.appendChild(inputField);
        removeTechnicalFields(frm);
        frm.submit();
    }


    // Event Listeners
    document.addEventListener('DOMContentLoaded', () => {
        // adds other listeners only when DOM is loaded
        recalculate();
        let items = document.getElementsByClassName('cart-item');
        let sku = "";
        for (let i = 0; i < items.length; i++) {
            sku = items[i].dataset.sku;
            document.getElementById(sku + "-minus").addEventListener('click', (e) => {
                let sku = e.target.id.split("-")[0];
                decrQty(sku);
            })
            document.getElementById(sku + "-plus").addEventListener('click', (e) => {
                let sku = e.target.id.split("-")[0];
                incrQty(sku);
            })
            document.getElementById(sku + "-qty").addEventListener('change', (e) => {
                let sku = e.target.id.split("-")[0];
                setQty(sku);
            })
        }
        document.getElementById('shipping').addEventListener('change', (e) => {
            recalculate();
        })
        document.getElementById('update-cart-bt').addEventListener('click', (e) => {
            updateCart();
        })
        document.getElementById('checkout-bt').addEventListener('click', (e) => {
            checkout();
        })

    })
} // EOF main

cart();