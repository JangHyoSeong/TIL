from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    price   = models.IntegerField()
    location = models.CharField(max_length=100)
    participants = models.ManyToManyField('Participant', through='Attendance')

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    num_of_participants = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)
    events = models.ManyToManyField('Event', through='Attendance')

    def __str__(self):
        return self.name

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    total_fee =models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()

    def __str__(self):
        return f'{self.participant} - {self.event}'

