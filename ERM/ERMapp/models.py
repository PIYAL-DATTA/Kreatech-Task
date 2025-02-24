from django.db import models

# Create your models here.


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.role} - {self.country} - {self.nationality} - {self.religion} - {self.gender} - {self.email}"


class Post(models.Model):
    role = models.CharField(max_length=255, primary_key=True)
    starting = models.DateField(max_length=255)
    ending = models.DateField(max_length=255)

    def __str__(self):
        return f"{self.role} - {self.starting} - {self.ending}"
