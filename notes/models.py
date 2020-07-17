from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    tickets = models.ForeignKey('tickets.Ticket',on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    content = models.TextField(blank= False, null = False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} note added by {1} on {2}".format(self.ticket, self.user, self.creation_date)
