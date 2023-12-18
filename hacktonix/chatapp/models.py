from django.db import models

# Create your models here.
# models.py

from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username


class Message(models.Model):
    sender = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.timestamp}"
