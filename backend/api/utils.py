def get_cloudpayment_data(request):
    data = {
        "email": request.data.get("receipt_email"),
        "donat": request.data.get("amount"),
        "payment_method": request.data.get("payment_method"),
        "payment_status": request.data.get("status"),
        "currency": request.data.get("currency"),
    }
    return data
