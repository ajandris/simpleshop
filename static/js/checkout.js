/**
 * Checkout Logic
 *
 * This file contains the main logic for the checkout page.
 *
 * Functions:
 * - checkout(): Initializes the checkout page, sets up event listeners for the payment button,
 *   and handles the simulated payment processing animation and alert.
 *
 * Intended functionality:
 * - Handle form validation for shipping and billing information.
 * - Integrate with a real payment gateway API.
 * - Manage the order summary display during the checkout flow.
 */
function checkout() {

    function handlePaymentClick(e) {
        e.preventDefault();
        const payButton = e.currentTarget;
        const originalText = payButton.innerHTML;
        payButton.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Processing...';
        payButton.style.opacity = '0.8';

        setTimeout(() => {
            alert('This is a demo checkout. Payment would be processed here.');
            payButton.innerHTML = originalText;
            payButton.style.opacity = '1';
        }, 1500);
    }

    function onDOMContentLoaded() {
        console.log('Checkout loaded');

        const payButton = document.querySelector('.pay-button');
        if (payButton) {
            payButton.addEventListener('click', handlePaymentClick);
        }
    }

    document.addEventListener('DOMContentLoaded', onDOMContentLoaded);
}

checkout();
