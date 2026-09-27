from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Event, Registration
from .forms import RegistrationForm


# Dashboard
@login_required
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


# Events page
@login_required
def events(request):

    events = Event.objects.all().order_by(
        'date',
        'time'
    )

    return render(
        request,
        'events/event_list.html',
        {
            'events': events
        }
    )


# Add Event
@login_required
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


# Event List
@login_required
def event_list(request):

    events = Event.objects.all().order_by(
        'date',
        'time'
    )

    return render(
        request,
        'events/event_list.html',
        {
            'events': events
        }
    )


# Register for Event
@login_required
def register_event(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )

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

            registration = form.save(
                commit=False
            )

            registration.event = event

            registration.save()

            return redirect(
                'registration_success'
            )

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
@login_required
def registration_success(request):

    return render(
        request,
        'events/registration_success.html'
    )


# Organizer Dashboard
@login_required
def organizer_dashboard(request):

    events = Event.objects.all().order_by(
        'date',
        'time'
    )

    for event in events:

        event.registration_count = Registration.objects.filter(
            event=event
        ).count()

        event.registrations = Registration.objects.filter(
            event=event
        ).order_by(
            '-registered_at'
        )

    return render(
        request,
        'events/organizer_dashboard.html',
        {
            'events': events
        }
    )


# Event Details
@login_required
def event_detail(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )

    event.registration_count = Registration.objects.filter(
        event=event
    ).count()

    event.remaining_seats = (
        event.max_participants
        - event.registration_count
    )

    return render(
        request,
        'events/event_detail.html',
        {
            'event': event
        }
    )


# Participants
@login_required
def participants(request):

    registrations = Registration.objects.all().order_by(
        '-registered_at'
    )

    return render(
        request,
        'events/participants.html',
        {
            'registrations': registrations
        }
    )


# Analytics
@login_required
def analytics(request):

    events = Event.objects.all().order_by(
        'date',
        'time'
    )

    total_events = Event.objects.count()

    total_participants = Registration.objects.count()

    total_seats = sum(
        event.max_participants
        for event in events
    )

    available_seats = (
        total_seats
        - total_participants
    )

    for event in events:

        event.registration_count = Registration.objects.filter(
            event=event
        ).count()

        event.remaining_seats = (
            event.max_participants
            - event.registration_count
        )

        if event.max_participants > 0:

            event.percentage = (
                event.registration_count * 100
            ) // event.max_participants

        else:

            event.percentage = 0

    return render(
        request,
        'events/analytics.html',
        {
            'events': events,
            'total_events': total_events,
            'total_participants': total_participants,
            'total_seats': total_seats,
            'available_seats': available_seats,
        }
    )


# Notifications
@login_required
def notifications(request):

    notifications = []

    # New registrations
    recent_registrations = Registration.objects.all().order_by(
        '-registered_at'
    )[:5]

    for registration in recent_registrations:

        notifications.append({
            'icon': '👥',
            'title': 'New Registration',
            'message': (
                registration.student_name
                + ' registered for '
                + registration.event.name
            )
        })

    # Upcoming events
    upcoming_events = Event.objects.filter(
        date__gte=timezone.now().date()
    ).order_by(
        'date',
        'time'
    )[:5]

    for event in upcoming_events:

        notifications.append({
            'icon': '📅',
            'title': 'Upcoming Event',
            'message': (
                event.name
                + ' is scheduled on '
                + str(event.date)
            )
        })

    return render(
        request,
        'events/notifications.html',
        {
            'notifications': notifications
        }
    )