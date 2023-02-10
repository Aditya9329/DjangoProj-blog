from django.urls import path
from .import views
urlpatterns = [
    path('',views.signup),
    path('signin/',views.signin),
    path('blogpage/',views.blogpage)
]