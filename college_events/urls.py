from django.contrib import admin
from django.urls import path
from events.views import (
    dashboard,
    events,
    add_event,
    event_list,
    register_event,
    registration_success
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Dashboard
    path("", dashboard, name="dashboard"),

    # Events
    path("events/", events, name="events"),
    path("events/add/", add_event, name="add_event"),

    # Event List
    path("event-list/", event_list, name="event_list"),

    # Registration
    path(
        "events/register/<int:event_id>/",
        register_event,
        name="register_event"
    ),

    path(
        "registration-success/",
        registration_success,
        name="registration_success"
    ),
]