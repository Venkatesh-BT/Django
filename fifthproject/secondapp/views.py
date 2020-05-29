from django.shortcuts import render
from django.http import HttpResponse
def display_data2(request):
	data='<h1>This is firstapp function</h1>'
	return HttpResponse(data)


# Create your views here.
