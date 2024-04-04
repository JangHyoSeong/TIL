from django.shortcuts import render, redirect
from .models import Store, Product
from .forms import StoreForm, ProductForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    form = ProductForm()
    context = {
        'store': store,
        'form' : form,
    }
    return render(request, 'stores/detail.html', context)

def create_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect('stores:detail', store.pk)
    else:
        form = StoreForm()
    context = {
        'form' : form,
    }
    return render(request, 'stores/create.html', context)

def create_product(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.store = store
        product.save()
        return redirect('stores:detail', store_pk)
    return redirect('stores:detail', store_pk)