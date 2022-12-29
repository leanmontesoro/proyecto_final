from django.urls import path
from AppLogin.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("login/", login_req, name="login"),
    #path('logout/', LogoutView.as_view(), name='logout'),

]