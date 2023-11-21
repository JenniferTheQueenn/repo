# forms.py

from django import forms

from .models import Contact


from django import forms
from .models import Contact  # Make sure to import your Contact model

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'profession1': forms.TextInput(),
            'profession2': forms.TextInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        profession1 = cleaned_data.get('profession1')
        profession2 = cleaned_data.get('profession2')

        if profession1 and profession2 and profession1 != profession2:
            raise forms.ValidationError("Professions do not match. Please enter them again.")

        return cleaned_data

class UpdateContactForm(forms.ModelForm):
    contact_id = forms.CharField(max_length=20) #new
    class Meta:
        model = Contact
        fields = ['name', 'address', 'profession', 'telephone', 'email']

class DeleteContactForm(forms.Form):
    contact_id = forms.CharField(max_length=20)

class ReadContactForm(forms.Form):
    contact_id = forms.CharField(max_length=20)
    
    
#class RequestIdForm(forms.Form):
 #   contact_id = forms.CharField(max_length=20)



