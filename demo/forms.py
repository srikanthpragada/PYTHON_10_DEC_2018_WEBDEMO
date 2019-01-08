import django.forms as forms


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50, required=False)
    price = forms.IntegerField(required=False)
