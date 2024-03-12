from django.db import models
from django.contrib.auth.models import User

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    login_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=20)
    browser_fingerprint = models.TextField()
    event = models.CharField(max_length=255)  # Nowe pole

    def __str__(self):
        return f'Event: {self.event} by {self.user.username} on {self.login_date}'
