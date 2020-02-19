from django.shortcuts import render
from .forms import PizzaForm


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    new_form = ""
    note = ""
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks for ordering! Your %s %s and %s pizza is on it\'s way!' % (filled_form.cleaned_data['size'],
                                                                                      filled_form.cleaned_data['topping1'].capitalize(
            ),
                filled_form.cleaned_data['topping2'].capitalize(),)
            new_form = PizzaForm
        return render(request, 'pizza/order.html', {'pizzaform': new_form, 'note': note})

    else:
        new_form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': new_form})
