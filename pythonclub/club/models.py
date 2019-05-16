from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_lengtoh=255)
    meetingagenda=models.CharField(max_length=255, null=True, blank=True)

def __str__(self):
    return self.meetingtitle

class Meta:
    db_table='meeting'

class MeetingMinutes(models.Model):
    meetingminutesname=models.CharField(max_length=255)
    meetingminutesid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingminutesattendance=models.ManyToManyField(User)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    meetingtext=models.CharField(max_length=255)

def __str__(self):
    return self.meetingminutesname

class Meta:
    db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    resourcedate=models.DateField()
    resourceuser=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.CharField(max_length=255)
    user=models.ManyToManyField(User)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitlename=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.CharField(max_length=255, null=True, blank=True)
    eventuserid=models.ManyToManyField(User)

    def __str__(self):
        return self.eventtitlename

    class Meta:
        db_table='event'



    