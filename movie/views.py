from django.shortcuts import render,  get_object_or_404 , redirect, reverse
from .models import Movie, Reservation, ShowTime
# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        
        movie = Movie.objects.all()
        reser = Reservation.objects.filter(user = request.user)
        
        if request.method == "POST":
            reservation_id = request.POST.get("reser_id")
            # print(reservation_id)
            reservation = Reservation(user=request.user, id = reservation_id )
            reservation.delete()
            
        
        return render(request, "dashboard.html", {"movie": movie, "reser":reser})
    else:
        return redirect("user:login")

 



def showtime_view (request, id):
    
    if request.user.is_authenticated:  
        movie = Movie.objects.get(id = id)
        print(movie)
        shows =  ShowTime.objects.filter(movie=movie)
        
        print (shows)
        print(shows)
        return render (request, "showtime.html", {"shows": shows} )
    else:
        return redirect("user:login")
    








def res_view(request,id):
    if request.user.is_authenticated:  
        shows = ShowTime.objects.get(id = id)
        reser =  Reservation.objects.filter(show_time= shows)
        total_seats = shows.total_seats
        
        # print(request.user)
        # print(reser)
        # for r in reser:
        #     print(r.user)
        
        booked_seat_no = [reservation.seat_no for reservation in reser]
        
        ur_reser = Reservation.objects.filter(show_time = shows, user= request.user)
        print(ur_reser)
        
        total_booked_seats =  0
        
        for r in reser:
            total_booked_seats += 1      
            
        available_seats = total_seats - total_booked_seats
        
      
        ur_reser_seats = [reservation.seat_no for reservation in ur_reser]
        print (ur_reser_seats)
        print (booked_seat_no)
        
        
        total_seats_range =    range(1, total_seats +1)
        
        
        
        
        if request.method == 'POST':
            seat_no = request.POST.get('seat_no')
            if seat_no  not in booked_seat_no:
                Reservation.objects.create(user= request.user, show_time = shows, seat_no = seat_no)
                return redirect(reverse("movie:reservation", kwargs={'id': id}))
        
        return render (request, "reservation.html", {
            "reser": reser, 
            "total_seats": total_seats, 
            "total_seats_range":total_seats_range,
            "total_booked_seats": total_booked_seats,
            "booked_seat_no": booked_seat_no,
            "available_seats":available_seats,
            "ur_reser": ur_reser,
            "ur_reser_seats": ur_reser_seats})
        
        
    else:
        return redirect("user:login")
    
    
