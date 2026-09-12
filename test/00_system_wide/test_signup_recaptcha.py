from unittest.mock import patch
import pytest
from django.conf import settings
from django.test import RequestFactory
from django.urls import reverse

from home.context_processors import recaptcha
from home.forms import CustomSignupForm


def test_recaptcha_context_processor():
    """Test that the recaptcha context processor returns the site_key."""
    factory = RequestFactory()
    request = factory.get("/")
    context = recaptcha(request)
    assert "site_key" in context
    assert context["site_key"] == getattr(settings, "RECAPTCHA_SITE_KEY", "")


@pytest.mark.django_db
def test_signup_page_renders_recaptcha(client):
    """Test that the signup page HTML renders the reCAPTCHA widget and script."""
    url = reverse("account_signup")
    response = client.get(url)
    assert response.status_code == 200

    content = response.content.decode("utf-8")
    assert "g-recaptcha" in content
    assert 'data-sitekey="' in content
    assert "https://www.google.com/recaptcha/api.js" in content


@pytest.mark.django_db
def test_signup_form_recaptcha_failure():
    """Test that signup form validation fails when reCAPTCHA verification fails."""
    form_data = {
        "username": "newuser123",
        "email": "newuser@example.com",
        "email2": "newuser@example.com",
        "password1": "ComplexP@ssw0rd!2026",
        "password2": "ComplexP@ssw0rd!2026",
        "g-recaptcha-response": "invalid-token",
    }

    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = {"success": False}
        form = CustomSignupForm(data=form_data)
        is_valid = form.is_valid()
        assert is_valid is False
        assert "reCAPTCHA failed. Please try again." in form.non_field_errors()


@pytest.mark.django_db
def test_signup_form_recaptcha_success():
    """Test that signup form passes reCAPTCHA validation when Google confirms success."""
    form_data = {
        "username": "validuser123",
        "email": "validuser@example.com",
        "email2": "validuser@example.com",
        "password1": "ComplexP@ssw0rd!2026",
        "password2": "ComplexP@ssw0rd!2026",
        "g-recaptcha-response": "valid-token",
    }

    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = {"success": True}
        form = CustomSignupForm(data=form_data)
        is_valid = form.is_valid()
        assert is_valid is True
        assert "reCAPTCHA failed. Please try again." not in form.non_field_errors()
