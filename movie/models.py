from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField( max_length=50)
    des = models.CharField( max_length=50)
    durtion = models.DurationField()
    
    def __str__(self):
        return self.title
    
    
class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField( auto_now=False, auto_now_add=False)
    total_seats = models.IntegerField()
    
    def __str__(self):
        return f"{self.movie.title} - {self.start_time}  "
    
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    seat_no = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.user.username} - {self.show_time.movie.title} - {self.show_time.start_time} - {self.seat_no}"
    
    
    
    