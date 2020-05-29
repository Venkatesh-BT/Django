from django.shortcuts import render
from inputapp.forms import employee
def create_page(request):
	emp_page=employee()
	if request.method=="POST":
		emp_data=employee(request.POST)

		if emp_data.is_valid():
			print(f'Name is:{emp_data.cleaned_data["ename"]}')
			print(f'Salary is:{emp_data.cleaned_data["salary"]}')
			print(f'Email is:{emp_data.cleaned_data["email_id"]}')
	my_dict={'emp_page':emp_page}
	return render(request=request, template_name='html/display.html',context=my_dict)

# Create your views here.
