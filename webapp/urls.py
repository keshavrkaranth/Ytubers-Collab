from django.urls import path
from . import views


app_name = 'webapp'
urlpatterns = [
    path('', views.hello, name='hello'),
    path('about', views.about, name='about'),
    path('tubers', views.tubers, name='tubers'),
    path('contactus', views.contactus, name='contactus'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
]
