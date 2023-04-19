from django.forms import ModelForm
from appCrud.models import Carros

# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ["modelo", "marca", "ano"]
