# zarinpal request handler
from django.conf import settings
from suds.client import Client


def zarinpal_request_handler(
    merchant_id, amount, detail, user_email, user_phone_number, callback
):
    client = Client(settings.ZARINPAL["gateway_request_url"])
    result = client.service.PaymentRequest(
        merchant_id, amount, detail, user_email, user_phone_number, callback
    )
    if result.Status == 100:
        return (
            "https://sandbox.zarinpal.com/pg/StartPay/" + result.Authority,
            result.Authority,
        )
    else:
        return None, None


def zarinpal_payment_checker(merchant_id, amount, authority):
    client = Client(settings.ZARINPAL["gateway_request_url"])
    result = client.service.PaymentVerification(merchant_id, authority, amount)
    is_paid = True if result.Status in [100, 101] else False
    return is_paid, result.RefID
