from django.shortcuts import render

# Create your views here.

def home(request):
	context = {"test": "Karthik"}
	template = 'base.html'
	return render(request,template,context)