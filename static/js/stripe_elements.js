// This is your test publishable API key.
async function stripe_fnc(){

  function get_server(){
    return window.location.origin;
  }

  const response = await fetch("/payment/stripe/pk/", {method: "POST"});
  const pk = await response.json();

  const stripe = Stripe(pk.pk);

  const paymentElementOptions = {
  layout: "tabs", // Use 'tabs' or 'accordion'
  fields: {
    billingDetails: {
      address: {
        country: 'never', // Hides the country field
        postalCode: 'never', // Hides the postcode field
        },
      },
    },
  };

  let elements;

  initialize();

  let frm = document.getElementById('payment-form');
  if (frm) {
      frm.addEventListener("submit", handleSubmit);
      // console.log("Stripe form listener attached successfully.");
  } else {
      console.warn("Stripe Warning: Element 'payment-form' was not found on this page.");
  }
  // Fetches a payment intent and captures the client secret
  async function initialize() {
    const cartNoRaw = document.getElementById('cart_no').textContent;
    const cartNo = JSON.parse(cartNoRaw);
    const response = await fetch(`/payment/stripe/stripe_payment_intent/${cartNo}/`, {
        method: "POST"});
    const { clientSecret } = await response.json();

    const appearance = {
      theme: 'stripe',
      variables: {
        // colorPrimary: '#0570de',
        colorBackground: '#F5F0E6',
        // colorText: '#30313d',
        colorDanger: '#df1b41',
        // fontFamily: 'Ideal Sans, system-ui, sans-serif',
        spacingUnit: '2px',
        borderRadius: '4px',
        },
      rules: {
        '.Label': {
          fontWeight: '600',
          fontFamily: 'Verdana, sans-serif',
          fontSize: '12px',
          color: '#000000',
          display: 'block',
        }
      }
      };
    elements = stripe.elements(
        {
          appearance,
          clientSecret,
        });

    const paymentElement = elements.create("payment", paymentElementOptions);

    paymentElement.mount("#card-element");
  }

  async function handleSubmit(e) {
    e.preventDefault();
    // setLoading(true);

    // check address and name form
    const form = document.getElementById('addresses_form');
    const form_2 = document.getElementById('contact_information_form');

    const errorColor = "#df1b41";
    let isFormValid = true;
    let inputs = form.querySelectorAll('input[required]');
    let inputs_2 = form_2.querySelectorAll('input[required]');

    const allInputs = Array.from(inputs);
    for (let inp of inputs_2){
      allInputs.push(inp);
    }

    allInputs.forEach(input => {
        const errorDisplay = input.parentElement.querySelector('.error-message');

        if (!input.validity.valid) {
            isFormValid = false;
            input.classList.add('input-error');
            errorDisplay.textContent = input.validationMessage; // Use browser's default message
            errorDisplay.classList.add('error-text');

            // 2. Put error message under the field
            if (errorDisplay) {
                errorDisplay.textContent = "This field is required.";
                errorDisplay.style.color = errorColor;
                errorDisplay.style.fontSize = "12px";
            }
        } else {
          // Reset styles if the field is now valid
          input.classList.remove('input-error');
          errorDisplay.textContent = "";
        }
    });
    if (!isFormValid){
      return;
    }

    // creating order
    const address = (document.getElementById('address_line1') + ' ' +
        document.getElementById('address_line2')).trim();
    const city = document.getElementById('city') ? '' : document.getElementById('city');
    const postalCode = document.getElementById('zip') ? '' : document.getElementById('zip');
    const country = document.getElementById('country');

    const data = Array();

    const orderInfo = await fetch(`/payment/get_order/`, {
        method: "POST",
    });

    const email = '';
    const orderNo = 'fake-order-232-23213-3221323-233';
    const orderName = document.getElementById('first_name') + ' ' + document.getElementById('second_name')

    // Stripe payment
    const { error } = await stripe.confirmPayment({
      elements,
      confirmParams: {
        // Make sure to change this to your payment completion page
        return_url: `${get_server()}/payment/stripe/process_payment/`,
        payment_method_data: {
          billing_details: {
            name: orderName, // You can get this from a standard HTML input
            email: email,
            address: {
              line1: address,
              city: city,
              postal_code: postalCode,
              country: country,
            },
          },
          metadata: {
            order_number: orderNo,
          }
        },
      },
    });

    // This point will only be reached if there is an immediate error when
    // confirming the payment. Otherwise, your customer will be redirected to
    // your `return_url`. For some payment methods like iDEAL, your customer will
    // be redirected to an intermediate site first to authorize the payment, then
    // redirected to the `return_url`.
    if (error.type === "card_error" || error.type === "validation_error") {
      showMessage(error.message);
    } else {
      showMessage("An unexpected error occurred.");
    }

    // setLoading(false);
  }

  // ------- UI helpers -------

  function showMessage(messageText) {
    const messageContainer = document.querySelector("#payment-message");

    messageContainer.classList.remove("hidden");
    messageContainer.textContent = messageText;

    setTimeout(function () {
      messageContainer.classList.add("hidden");
      messageContainer.textContent = "";
    }, 4000);
  }

  // Show a spinner on payment submission
  // function setLoading(isLoading) {
  //   if (isLoading) {
  //     // Disable the button and show a spinner
  //     document.querySelector("#submit").disabled = true;
  //     document.querySelector("#spinner").classList.remove("hidden");
  //     document.querySelector("#button-text").classList.add("hidden");
  //   } else {
  //     document.querySelector("#submit").disabled = false;
  //     document.querySelector("#spinner").classList.add("hidden");
  //     document.querySelector("#button-text").classList.remove("hidden");
  //   }
  // }
}

document.addEventListener('DOMContentLoaded', async () => {
    await stripe_fnc();
});