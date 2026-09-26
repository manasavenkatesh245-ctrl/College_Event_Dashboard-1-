from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration
from .forms import RegistrationForm


# Dashboard
def dashboard(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'events/dashboard.html', {'events': events})


# Events page
def events(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'events/event_list.html', {'events': events})


# Add Event
def add_event(request):
    if request.method == 'POST':
        Event.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            venue=request.POST.get('venue'),
            organizer=request.POST.get('organizer'),
            max_participants=request.POST.get('max_participants')
        )

        return redirect('events')

    return render(request, 'events/add_event.html')


# Event List
def event_list(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'events/event_list.html', {'events': events})


# Register for Event
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()

            return redirect('registration_success')

    else:
        form = RegistrationForm()

    return render(
        request,
        'events/register.html',
        {
            'form': form,
            'event': event
        }
    )


# Registration Success
def registration_success(request):
    return render(
        request,
        'events/registration_success.html'
    )