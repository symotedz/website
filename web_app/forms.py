from django.forms import ModelForm
from . models import *

class EnquiryForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'