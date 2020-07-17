from django.shortcuts import render, get_object_or_404, redirect, reverse
from allauth.account.decorators import verified_email_required
from django.contrib import messages
from django.db.models import Q
from .models import Ticket
from .forms import AddForm
from notes.models import Note
from notes.forms import AddNoteForm

# Create your views here.


@verified_email_required
def tickets(request):
    """
    Renders a page showing all currently open tickets
    """
    tickets = Ticket.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.success(request, "Ticket Not Found")
                return redirect(reverse('tickets'))
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            tickets = tickets.filter(queries)

    context = {
        'tickets': tickets,
        'search_term': query,
    }

    return render(request, 'tickets.html', context)


@verified_email_required
def viewticket(request, ticket_id):
    """
    Renders a page showing one specific ticket taking the ticket
    ID as a parameter
    """

    ticket = get_object_or_404(Ticket, pk=ticket_id) if ticket_id else None

    ticket_notes = Note.objects.filter(tickets_id=ticket_id).order_by('-creation_date')

    if request.method == "POST":
        add_note_form = AddNoteForm(request.POST)
        if add_note_form.is_valid():
            note = add_note_form.save(commit=False)
            note.tickets = ticket_id
            note.user = request.user
            note.save()
            return redirect('viewticket', ticket_id=ticket_id)
        else:
            messages.error(request, "The operation was unsuccessful")
    else:
        add_note_form = AddNoteForm()

    context = {
        'ticket': ticket,
        'add_note_form': add_note_form,
        'notes': ticket_notes,
    }

    return render(request, 'viewticket.html', context)


@verified_email_required
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
