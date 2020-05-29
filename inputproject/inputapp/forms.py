from django import forms
class employee(forms.Form):
	ename = forms.CharField()
	salary = forms.IntegerField()
	email_id = forms.CharField()   
	 # TODO: Define form fields here
