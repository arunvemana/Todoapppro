from django.db import models

# Create your models here.

class todolist(models.Model):
    username = models.CharField(max_length=200)
    item = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)


class tododata(models.Model):
    username = models.CharField(max_length=200)
    item = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)