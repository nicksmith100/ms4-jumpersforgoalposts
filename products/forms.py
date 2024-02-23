from django import forms
from .models import Product, League, Team, Condition
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        leagues = League.objects.all()
        teams = Team.objects.all()
        conditions = Condition.objects.all()
        league_friendly_names = [(l.id, l.get_friendly_name()) for l in leagues]
        team_friendly_names = [(t.id, t.get_friendly_name()) for t in teams]
        condition_friendly_names = [(c.id, c.get_friendly_name()) for c in conditions]
        league_friendly_names.insert(0,("", "Select"))
        team_friendly_names.insert(0,("", "Select"))
        condition_friendly_names.insert(0,("", "Select"))
        self.fields['league'].choices = league_friendly_names
        self.fields['team'].choices = team_friendly_names
        self.fields['condition'].choices = condition_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'custom-form-input form-control my-2'
