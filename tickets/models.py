from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    '''
    A single Ticket
    '''
    TYPE_CHOICES = (
        ('bug', 'Bug Report'),
        ('feature', 'Feature Request'),
    )

    STATUS_CHOICES = (
        ('opened', 'Opened'),
        ('closed', 'Closed'),
    )

    title = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    description = models.TextField()
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="opened")
    creation_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return "{0} -- Type: {1} -- Status: {2} ".format(self.title, self.type, self.status)