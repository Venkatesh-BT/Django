from django.shortcuts import render
from django.http import HttpResponse
import datetime
def welcome_client(response):
	data=datetime.datetime.now()
	hour=int(data.strftime('%H'))
	msg='<body><marquee direction="down"><font color="red"><h1>Hey Client Good'
	if hour<12:
		msg+='Morning'
	elif hour<16:
		msg+='Afternoon'
	elif hour<19:
		msg+='Evening'
	else:
		msg+='Night'
	msg+='</h1></marquee><hr></body>'
	msg+='<h1>Server Time Is : '+str(data)+'</h1></body>'
	return HttpResponse(msg)
	# Create your views here.
