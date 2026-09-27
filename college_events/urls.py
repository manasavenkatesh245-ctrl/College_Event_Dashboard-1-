from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from events.views import (
    dashboard,
    events,
    add_event,
    event_list,
    register_event,
    registration_success,
    organizer_dashboard,
    event_detail,
    participants,
    analytics,
    notifications
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", dashboard, name="dashboard"),

    path("events/", events, name="events"),

    path("events/add/", add_event, name="add_event"),

    path("event-list/", event_list, name="event_list"),
    path(
    "login/",
    auth_views.LoginView.as_view(
        template_name="events/login.html"
    ),
    name="login"
),

path(
    "logout/",
    auth_views.LogoutView.as_view(),
    name="logout"
),

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
    path(
    "participants/",
    participants,
    name="participants"
),
path(
    "analytics/",
    analytics,
    name="analytics"
),
path(
    "notifications/",
    notifications,
    name="notifications"
),
]