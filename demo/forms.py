import django.forms as forms
from  django.forms import ModelForm
from . models import Book


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50, required=False)
    price = forms.IntegerField(required=False)

# Create a form from Model
class OrmAddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','price']

