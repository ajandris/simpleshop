/**
 * Checkout Logic
 *
 * This file contains the main logic for the checkout page.
 *
 * Functions:
 * - checkout(): Initializes the checkout page, sets up event listeners for the payment button,
 *   handles the simulated payment processing animation and alert, and calculates order totals.
 *
 * Intended functionality:
 * - Handle form validation for shipping and billing information.
 * - Integrate with a real payment gateway API.
 * - Manage the order summary display during the checkout flow.
 */

function checkout() {

    function showProductLinePrices(){
        const prodLines = document.getElementsByClassName("prod-line");
        let price = 0.00;
        let qty = 0;
        let total = 0.00;

        for (let pl of prodLines){
            price = Number(pl.dataset.price);
            qty = Number(pl.dataset.qty);
            total = price * qty;
            pl.textContent = total.toFixed(2);
        }
    }

    // Event Listeners
    document.addEventListener('DOMContentLoaded', () => {
        showProductLinePrices();
    })
}

checkout();
