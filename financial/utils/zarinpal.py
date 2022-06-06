



# zarinpal request handler
def zarinpal_request_handler(merchant_id, amount, detail, user_email, user_phone_number, callback):
    client = Client(settings.ZARINPAL['gateway_request_url'])
    result = client.service.PaymentRequest(
        merchant_id, amount, detail,
        user_email, user_phone_number, callback
    )
    if result.Status == 100:
        return 'https://sandbox.zarinpal.com/pg/StartPay/' + result.Authority, result.Authority
    else:
        return None, None