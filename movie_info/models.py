from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    movie_length = models.IntegerField(default=0)
    movie_release_date = models.DateField()
    
    def __str__(self):
        return "("+str(self.title)+","+str(self.description)+","+str(self.movie_length)+","+str(self.movie_release_date)+")"

class Category(models.Model):
    c_type = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    c_movie = models.ManyToManyField(Movie, through='Relationship')

    def __str__(self):
        return str(self.c_type)+" "+ str(self.value)


class Relationship(models.Model):
    taxonomy = models.ForeignKey(Category)
    r_movie = models.ForeignKey(Movie)

    def __str__(self):
        return str(self.taxonomy)+" "+ str(self.r_movie)

    

