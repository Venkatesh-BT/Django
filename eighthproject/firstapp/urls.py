from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('national_game/',views.national_game),
    path('national_animal/',views.national_animal),
    path('national_flower/',views.national_flower),

]