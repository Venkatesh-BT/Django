from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import json
@api_view(["POST"])
def fibo(num):
	prev=0
	cur=1
	n=json.loads(num.body)
	try:
		for i in range(n):
			if i==0:
				cur=i 
			elif i==1:
				cur=i 
			else:
				temp=cur
				cur=prev+cur
				prev=temp
		return Response({'the nth num is':cur})
	except Exception as e:
		return Response(e.args[0],status.HTTP_404_NOT_FOUND)


# Create your views here.
