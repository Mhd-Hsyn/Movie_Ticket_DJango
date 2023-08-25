from django.contrib import admin
from .models import Movie, Reservation, ShowTime
# Register your models here.


class Movie_admin(admin.ModelAdmin):
    list_display = ["id","title", "des", "durtion"]
    
class ShowTime_admin(admin.ModelAdmin):
    list_display = ["id","movie", "start_time", "total_seats"]
    

class Reservation_admin(admin.ModelAdmin):
    list_display = ["id","user", "show_time", "seat_no"]
    

admin.site.register(Movie, Movie_admin)            
admin.site.register(ShowTime, ShowTime_admin )            
admin.site.register(Reservation,Reservation_admin)            