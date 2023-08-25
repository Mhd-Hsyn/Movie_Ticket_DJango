
from django.urls import path, include
from movie import urls
from . import views
app_name = "user"

urlpatterns = [
    path("register/", views.register , name= "register"),
    path("login/", views._login, name="login"),
    # path('movie/', include('movie.urls')),  # Include the app's urls.py here

    
    
]
