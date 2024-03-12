from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UserActivity

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip_address = request.META.get('REMOTE_ADDR')
    browser_fingerprint = request.META.get('HTTP_USER_AGENT', '')  # Prosty sposób na fingerprint
    event = "logged on"  # Stała wartość dla tego zdarzenia
    UserActivity.objects.create(user=user, ip_address=ip_address, browser_fingerprint=browser_fingerprint, event=event)
