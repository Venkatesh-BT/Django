from django.shortcuts import render
from django.http import HttpResponse
def national_game(request):
	data='<h1>The national game is Hockey</h1>'
	return HttpResponse(data)
def national_animal(request):
	data='<h1>The national animal is Tiger</h1>'
	return HttpResponse(data)
def national_flower(request):
	data='<h1>The national flower is Lotus</h1>'
	return HttpResponse(data)

# Create your views here.
