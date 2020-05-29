from django.shortcuts import render
import datetime
def display_time(request):
	data=datetime.datetime.now()
	my_dict={'time':data}
	return render(request=request, template_name='display.html',context=my_dict)

# Create your views here.
