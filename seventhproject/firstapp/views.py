from django.shortcuts import render
import datetime
def display_data(request):
	data=datetime.datetime.now()
	print(data)
	my_dict={'insert_time':data,'Name':'Venkatesh','Age':23,'Email':'vbtimmanagoudar45@gmail.com'}
	return render(request=request, template_name='firstapp/display.html',context=my_dict)

# Create your views here.
