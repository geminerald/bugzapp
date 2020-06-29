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