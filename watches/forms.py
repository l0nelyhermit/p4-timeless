from django import forms
from .models import Watch


class NewWatch(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('watch_brand', 'watch_model', 'description', 'watch_price')
