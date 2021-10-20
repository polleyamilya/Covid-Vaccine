from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from covid1.users.models import covidvacc,State


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class covidForm(forms.ModelForm):
    class Meta:
        model = covidvacc
        fields = ('name', 'Age', 'District','State')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['State'].queryset = State.objects.none()

        if 'District' in self.data:
            try:
                District_id = int(self.data.get('District'))
                self.fields['State'].queryset = State.objects.filter(District_id=District_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['State'].queryset = self.instance.district.state_set.order_by('name')