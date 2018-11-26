from django.db import models

from polls.models import User


class Blacklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starting_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.user.username
