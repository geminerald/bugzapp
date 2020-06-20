from django.shortcuts import render, get_object_or_404
from .models import Ticket

# Create your views here.


def tickets(request):
    """
    Renders a page showing all currently open tickets
    """
    tickets = Ticket.objects.all()

    context = {
        'tickets': tickets,
    }

    return render(request, 'tickets.html', context)


def viewticket(request, ticket_id):
    """
    Renders a page showing one specific ticket
    """

    ticket = get_object_or_404(Ticket, pk=ticket_id)

    context = {
        'ticket': ticket,
    }

    return render(request, 'viewticket.html', context)
