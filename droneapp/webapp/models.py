from django.db import models

class Drone_info(models.Model):
    controller_state = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    velocity = models.FloatField()
    batery = models.FloatField()
    timestamp = models.DateTimeField()
    id_fly_history = models.ForeignKey('Drone_info', on_delete=models.CASCADE)

class Fly_history(models.Model):
    time_start = models.DateTimeField()
    time_end = models.DateTimeField(null=True)
