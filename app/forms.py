from app.models import Person
from django.forms import ModelForm

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'patronymic', 'sex', 'category', 'division']
