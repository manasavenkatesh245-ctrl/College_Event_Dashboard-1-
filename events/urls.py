from django.contrib import admin
from django.urls import path

from events.views import (
    dashboard,
    events,
    add_event,
    event_list,
    register_event,
    registration_success,
    organizer_dashboard,
    event_detail
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", dashboard, name="dashboard"),

    path("events/", events, name="events"),

    path("events/add/", add_event, name="add_event"),

    path("event-list/", event_list, name="event_list"),

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

    path(
        "organizer/",
        organizer_dashboard,
        name="organizer_dashboard"
    ),

    path(
        "event/<int:event_id>/",
        event_detail,
        name="event_detail"
    ),
]