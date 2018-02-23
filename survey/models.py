from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=25)
    country = models.CharField(max_length=15)
    vote = models.IntegerField()

    def __str__(self):
        return self.name
