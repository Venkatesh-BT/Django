from django.shortcuts import render
from cricapp.models import player
def select_records(request):
	lst=player.objects.all()
	my_dict={'lst':lst}
	return render(request=request, template_name='html/display.html',context=my_dict)
# Create your views here.
