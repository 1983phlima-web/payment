
import os
import stripe
from flask import Flask, render_template, jsonify

# Configuração da chave de API do Stripe
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "sk51Hh2xLExR27A5s5FqV2jE4g2fB6g3h7g8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6A7B8C9D0E1F2")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("payStripe.html")

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    try:
        # ID da conta conectada do vendedor
        connected_account_id = "acct_1Hh2xLExR27A5s5F"

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "brl",
                        "product_data": {
                            "name": "Produto Exemplo",
                        },
                        "unit_amount": 10000,
                    },
                    "quantity": 1,
                }
            ],
            payment_intent_data={
                "application_fee_amount": 1000,  # Taxa de 10% para a plataforma (R$10,00)
                "transfer_data": {"destination": connected_account_id},
            },
            mode="payment",
            success_url="http://localhost:5000/success",
            cancel_url="http://localhost:5000/cancel",
        )
        return jsonify({"id": session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route("/success")
def success():
    return "Pagamento bem-sucedido!"

@app.route("/cancel")
def cancel():
    return "Pagamento cancelado."

if __name__ == "__main__":
    app.run(port=5000, debug=True)

