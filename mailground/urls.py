from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# URL config
urlpatterns = [
    path('', views.home),
    path('hello/', views.say_hello)
    # path('', views.home)
]