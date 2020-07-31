from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Business

class BusinessForm(ModelForm):

  class Meta:
    model = Business
    fields = ['name', 'link', 'description', 'email', 'contact_name', 'address', 'zipcode', 'state', 'country']

  def clean_business_form():
    #add form validation here; e.g. zipcode = self.cleaned_data.get('zipcode'); if not valid zipcode; raise forms.ValidationError("Invalid zipcode.")
    return super(BusinessForm, self).clean()