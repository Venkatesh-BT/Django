from django.shortcuts import render
from .forms import employeeForm
def save_page(request):
	emp_form=employeeForm()
	if request.method=="POST":
		emp_data=employeeForm(request.POST)

		if emp_data.is_valid():
			emp_data.save(commit=True)
	my_dict={'emp_form':emp_form}
	return render(request=request, template_name='html/display.html',context=my_dict)


# Create your views here.
