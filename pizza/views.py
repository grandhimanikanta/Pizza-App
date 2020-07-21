from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaForm
from django.forms import formset_factory


def home(request):
    return render(request,'home.html')

def order(request):
    multiple_form=MultiplePizzaForm()
    if request.method == 'POST':
        filled_form=PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            msg="Thanks for the Ordering the PIZZA"
            new_form=PizzaForm()
            return render(request, 'order.html', {'message':msg,'Pizzaform':new_form,'multiple_form':multiple_form})
    else:
        form=PizzaForm()
        return render(request,'order.html',{'Pizzaform':form,'multiple_form':multiple_form})
# Create your views here.
def pizzas(request):
    number_of_pizzas=2
    filled_multiple_form=MultiplePizzaForm(request.GET)
    if filled_multiple_form.is_valid():
        number_of_pizzas=filled_multiple_form.cleaned_data['number']
    Pizzaformset=formset_factory(PizzaForm,extra=number_of_pizzas)
    formset=Pizzaformset()
    if request.method == 'POST':
        filled_formset=Pizzaformset(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            message="Pizzas have been Ordered"
        else:
            message="your order was not created...please try again!"
        return render(request,'pizzas.html',{'message':message,'formset':formset})
    else:
        return render(request, 'pizzas.html', {'formset': formset})
