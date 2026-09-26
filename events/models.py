from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200)
    max_participants = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    student_email = models.EmailField()
    student_phone = models.CharField(max_length=15)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name + " - " + self.event.name
