from django import forms
from .models import Pizza,Size

class PizzaForm(forms.ModelForm):
    # size=forms.ModelMultipleChoiceField(queryset=Size.objects,widget=forms.CheckboxSelectMultiple)
    # Image=forms.ImageField()
    class Meta:
        model=Pizza
        fields=['topping1','topping2','size']
        labels={'topping1':'Topping 1','topping2':'Topping 2'}
class MultiplePizzaForm(forms.Form):
    number=forms.IntegerField(min_value=2,max_value=5)














# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label="topping 1",max_length=30)
#     topping2 = forms.CharField(label="topping 2", max_length=30)
#     Size = forms.ChoiceField(label='Size',choices=[['Small','Small'],['Medium','Medium'],['Large','Large']])
