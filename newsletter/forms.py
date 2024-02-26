from django import forms
from .models import Subscriber
from products.models import Team


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['autofocus'] = True

        teams = Team.objects.all()
        team_friendly_names = [(t.id, t.get_friendly_name()) for t in teams]
        choices = team_friendly_names
        choices.insert(0, ("", "Select"))
        choices.insert(1, (999, "Team not listed (insert below)"))

        self.fields['favourite_team'].choices = choices
        self.fields['other_team'].label = "Unlisted team"
        self.fields['team_news_only'].label = \
            "I only want emails about my favourite team"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = \
                'form-control my-2 custom-form-input'
