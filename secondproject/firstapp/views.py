from django.shortcuts import render
from django.http import HttpResponse
import datetime
def server_time(request):
	data=datetime.datetime.now()
	msg='<marquee direction="bottom"><font color="red"><h1>Server Time is : '+str(data)+'</h1></marquee>'
	return HttpResponse(msg)

# Create your views here.
