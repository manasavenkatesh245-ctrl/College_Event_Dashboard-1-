from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),

    path(
        'register/<int:event_id>/',
        views.register_event,
        name='register_event'
    ),

    path(
        'registration-success/',
        views.registration_success,
        name='registration_success'
    ),
]