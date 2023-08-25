from django.urls import path, include
from . import views
 path("logout/" , LogoutView.as_view(next_page = "movie:dashboard")),# from movie import urls
app_name = 'movie'

urlpatterns = [
    
    path("",views.dashboard , name= 'dashboard' ),
    path("logout/" , LogoutView.as_view(next_page = "movie:dashboard")),
    path("showtime/<int:id>" , views.showtime_view  ,name = "showtime"),
    path("reser/<int:id>", views.res_view, name ="reservation" )
]
