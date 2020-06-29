/*
Stripe setup

 */

const stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
const client_secret = $('#id_client_secret').text().slice(1,-1);
const stripe = Stripe(stripe_public_key);
const elements = stripe.elements();


var style = {
  base: {
    color: "#fff",
  }
};


const card = elements.create('card', {style: style});

card.mount('#card-element');

// Handle realtime validation errors on the card element

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error){
        var html = `
        <span class="icon" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    }else {
        errorDiv.textContent = '';
    }
})