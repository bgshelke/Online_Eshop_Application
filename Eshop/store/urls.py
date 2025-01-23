from django.urls import path
from .views import home,signup,login


urlpatterns = [
    path('',home.IndexView.as_view(),name='home_url'),
    path('signup/',signup.SignupView.as_view()),
    path('login/',login.LoginView.as_view())

]