from django.shortcuts import render
from django.http import HttpResponse
def display_data(request):
	data='<body bgcolor="blue"><marquee direction="up" ><font color="red"><b><i><h1>WELCOME</h1></i></b></marquee></body>'
	return HttpResponse(data)
# Create your views here.
