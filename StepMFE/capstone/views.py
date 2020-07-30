from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import BusinessForm

# Create your views here.
def index(request):
	return render(request, 'capstone/index.html')

def thanks(request):
	return render(request, 'capstone/thanks.html')

def add_business(request):
  form = BusinessForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.name = form.cleaned_data['name']
      form.link = form.cleaned_data['link']
      form.description = form.cleaned_data['description']
      form.email = form.cleaned_data['email']
      form.contact_name = form.cleaned_data['contact_name']
      form.address = form.cleaned_data['address']
      form.zipcode = form.cleaned_data['zipcode']
      form.state = form.cleaned_data['state']
      form.country = form.cleaned_data['country']
      form.save()
      return HttpResponseRedirect('/thanks')
  else: 
    form = BusinessForm()
  context = {
    'form': form,
    'form': form,
  }
  return render(request, 'capstone/add_business.html', context)