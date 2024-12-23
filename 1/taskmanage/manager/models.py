from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.DateField()
    status = models.CharField(max_length=10, choices=(('Pending', 'Pending'), ('Completed', 'Completed')))
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(Attendee, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
