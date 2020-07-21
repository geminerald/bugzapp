from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets, name="tickets"),
    path('view/<ticket_id>', views.viewticket, name="viewticket"),
    path('add/', views.addticket, name='addticket')
]
