from django.contrib import admin
from .models import Ticket
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    fields = ['title', 'type', 'status', 'score', 'description', ]
    readonly_fields = ['user', 'description']


admin.site.register(Ticket, TicketAdmin)
