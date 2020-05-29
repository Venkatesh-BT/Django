from django.shortcuts import render
def display_data(request):
	return render(request=request,template_name='firstapp/display.html')

# Create your views here.
