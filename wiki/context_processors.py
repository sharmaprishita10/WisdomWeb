from encyclopedia import util
from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}), label = "")

def data(request):
    return { "entries" : util.list_entries(), "form" : SearchForm() }