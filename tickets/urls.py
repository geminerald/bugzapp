from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets, name="tickets"),
    path('<ticket_id>', views.viewticket, name="viewticket")
]