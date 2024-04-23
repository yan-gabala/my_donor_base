from django import forms


class CloudPaymentsForm(forms.Form):
    """
    Форма для платежа через CloudPaymenent.
    """

    amount = forms.DecimalField(max_digits=6, decimal_places=2)
