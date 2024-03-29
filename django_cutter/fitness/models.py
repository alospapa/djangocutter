from django.db import models

# Create your models here.
class Set(models.Model):
    name = models.CharField(max_length=100)
    reps = models.IntegerField()
    weight = models.IntegerField()
    date = models.DateField()
    workout = models.ForeignKey('workout', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Workout(models.Model):
    name = models.CharField(max_length=100)   
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    name = models.CharField(max_length=100)   
    sets = models.ManyToManyField('Set')


    def __str__(self):
        return self.name


