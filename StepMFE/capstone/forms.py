from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Business, Search

class BusinessForm(ModelForm):

  class Meta:
    model = Business
    fields = ['name', 'link', 'category', 'description', 'email', 'contact_name', 'address', 'zipcode', 'state', 'country']

  def clean_business_form():
    #add form validation here; e.g. zipcode = self.cleaned_data.get('zipcode'); if not valid zipcode; raise forms.ValidationError("Invalid zipcode.")
    return super(BusinessForm, self).clean()

class SearchForm(ModelForm):

  class Meta:
    model = Search
    fields = ['category', 'state']

  def clean_search_form():
    return super(SearchForm, self).clean()
