from django.db import models

# Create your models here.


# Celery tasks
class Task(models.Model):
    pid = models.IntegerField()

    def __str__(self):
        return self.pid
