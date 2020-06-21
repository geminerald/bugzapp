from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .forms import AddForm

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
    Renders a page showing one specific ticket taking the ticket ID as a parameter
    """

    ticket = get_object_or_404(Ticket, pk=ticket_id)

    context = {
        'ticket': ticket,
    }

    return render(request, 'viewticket.html', context)


def addticket(request):

    if request.method == "POST":
        add_ticket_form = AddForm(request.POST, request.FILES)
        if add_ticket_form.is_valid():
            ticket = add_ticket_form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            ticket.user = request.user  # Set the user object here
            ticket.save()  # Now you can send it to DB
            return redirect('tickets')
    else:
        add_ticket_form = AddForm()
    return render(request, 'addticket.html', {'add_ticket_form': add_ticket_form})
