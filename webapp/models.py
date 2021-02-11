from django.db import models
import pytz

class Member(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    real_name=models.CharField(max_length=200, blank=True, null=True)
    tz = models.CharField(max_length=34, choices=TIMEZONES, default='UTC')
    
    def __str__(self):
        return str(self.real_name)

class Activity(models.Model):
    member=models.ForeignKey(Member,on_delete=models.CASCADE,related_name='activity_periods')
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def __str__(self):
        return str(self.member)
