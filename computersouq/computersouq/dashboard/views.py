from django.shortcuts import redirect, render
from .forms import AddLaptopsForm
from django.http import HttpResponse

def add_laptop(request):
    if request.method == 'POST':
        form = AddLaptopsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:addlaptop')
        else:
            print(form.errors)
    else:
        form = AddLaptopsForm()
    context = {'form': form}
    return render(request, 'add_laptop.html', context)
def debit_credit(request):
    pass