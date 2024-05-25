# models.py
from django.db import models

class Door(models.Model):
    door_id = models.AutoField(primary_key=True)
    door_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default='closed')

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    card_id = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=50)

class AccessLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    door = models.ForeignKey(Door, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    access_granted = models.BooleanField(default=False)
    action = models.CharField(max_length=10)  # 'entry' or 'exit'
