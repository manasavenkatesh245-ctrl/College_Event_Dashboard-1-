from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Event, Registration
from .forms import RegistrationForm


def dashboard(request):
    events = Event.objects.all().order_by('date', 'time')

    total_events = Event.objects.count()
    total_registrations = Registration.objects.count()

    upcoming_events = Event.objects.filter(
        date__gte=timezone.now().date()
    ).count()

    for event in events:
        event.registration_count = Registration.objects.filter(
            event=event
        ).count()

        event.remaining_seats = (
            event.max_participants - event.registration_count
        )

    return render(
        request,
        'events/dashboard.html',
        {
            'events': events,
            'total_events': total_events,
            'total_registrations': total_registrations,
            'upcoming_events': upcoming_events,
        }
    )


def events(request):
    events = Event.objects.all().order_by('date', 'time')

    return render(
        request,
        'events/event_list.html',
        {'events': events}
    )


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

    return render(
        request,
        'events/add_event.html'
    )


def event_list(request):
    events = Event.objects.all().order_by('date', 'time')

    return render(
        request,
        'events/event_list.html',
        {'events': events}
    )


def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():

            registration_count = Registration.objects.filter(
                event=event
            ).count()

            if registration_count >= event.max_participants:
                return render(
                    request,
                    'events/register.html',
                    {
                        'form': form,
                        'event': event,
                        'error': 'Registration is full for this event.'
                    }
                )

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


def registration_success(request):
    return render(
        request,
        'events/registration_success.html'
    )


def organizer_dashboard(request):
    events = Event.objects.all().order_by('date', 'time')

    for event in events:
        event.registration_count = Registration.objects.filter(
            event=event
        ).count()

        event.registrations = Registration.objects.filter(
            event=event
        ).order_by('-registered_at')

    return render(
        request,
        'events/organizer_dashboard.html',
        {'events': events}
    )