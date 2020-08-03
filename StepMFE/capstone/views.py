from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import BusinessForm, SearchForm
from .models import Business

def add_business(request):
  form = BusinessForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.name = form.cleaned_data['name']
      form.link = form.cleaned_data['link']
      form.category = form.cleaned_data['category']
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
      print(form.errors)
  else: 
    form = BusinessForm()

  context = {
    'form': form,
  }
  return render(request, 'capstone/add-business.html', context)

def index(request):
	return render(request, 'capstone/index.html')

def history(request):
    return render(request, 'capstone/history-page.html')

def thanks(request):
	return render(request, 'capstone/thanks.html')

def search(request):
  form = SearchForm(request.POST)
  if request.method == 'POST':
    businesses = Business.objects.all()
    if form.is_valid():
      if form.cleaned_data['category']:
        businesses = businesses.filter(category = form.cleaned_data['category'])
      if form.cleaned_data['keywords']:
        businesses = businesses.filter(description__icontains = form.cleaned_data['keywords'])
    context = {'businesses': businesses, 'form': form}
    return render(request, 'capstone/search.html', context)
  else: 
    form = SearchForm()
    context = {'form': form}
  return render(request, 'capstone/search.html', context)