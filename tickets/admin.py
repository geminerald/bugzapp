from django.contrib import admin
from .models import Ticket
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    fields = ['title', 'type', 'status', 'score', 'description', 'user']
    readonly_fields = ['user']


admin.site.register(Ticket, TicketAdmin)
