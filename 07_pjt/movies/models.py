from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100) #배우이름

class Movie(models.Model):
    title = models.CharField(max_length=100) #제목
    overview = models.TextField() #줄거리
    release_date = models.DateTimeField() 
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name ='movies')


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)




