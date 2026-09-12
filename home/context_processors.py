from django.conf import settings


def recaptcha(request):
    """
    Context processor to make reCAPTCHA site key available in templates.
    """
    return {
        "site_key": getattr(settings, "RECAPTCHA_SITE_KEY", ""),
    }
