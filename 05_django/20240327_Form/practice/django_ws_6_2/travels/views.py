from django.shortcuts import render, redirect
from .models import travels
from .forms import TravelsForm


# Create your views here.
def index(request):
    travel = travels.objects.all()
    context = {
        'travels' : travel,
    }
    return render(request, 'travels/index.html', context)


def create(request):
    if request.method == 'POST':
        form = TravelsForm(request.POST)
        if form.is_valid():
            travels = form.save()
        return redirect('travels:detail', travels.pk)
    else:
        form = TravelsForm()
    context = {
        'form' : form,
    }

    return render(request, 'travels/create.html', context)

def detail(request, pk):
    travel = travels.objects.get(pk=pk)
    context = {
        'travels' : travel,
    }
    return render(request, 'travels/detail.html', context)