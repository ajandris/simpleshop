import requests
from allauth.account.forms import SignupForm
from django import forms
from django.conf import settings


class CustomSignupForm(SignupForm):
    def clean(self):
        super().clean()
        recaptcha_response = self.data.get("g-recaptcha-response")

        data = {
            "secret": getattr(settings, "RECAPTCHA_SECRET_KEY", ""),
            "response": recaptcha_response,
        }

        try:
            r = requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data=data,
                timeout=10,
            )
            result = r.json()
        except requests.RequestException:
            result = {}

        if not result.get("success"):
            self.add_error(None, "reCAPTCHA failed. Please try again.")

        return self.cleaned_data
