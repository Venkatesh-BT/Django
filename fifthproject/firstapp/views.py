from django.shortcuts import render
from django.http import HttpResponse
def display_data1(request):
	data='<marquee direction="down"><font color:"red"><h1>This is firstapp function</h1></marquee>'
	return HttpResponse(data)


# Create your views here.
