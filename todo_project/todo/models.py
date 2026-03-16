from django.db import models

class Task(models.Model):
    title = models.Charfield(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# this model here stores the task title and the completed status
