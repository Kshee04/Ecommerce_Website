from django.shortcuts import render


# Create views
def store(request):
    context = {}
    return render(request, 'store.html', context)


def index(request):
    context = {}
    return render(request, 'index.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


def cart(request):
    context={}
    return render(request, 'cart.html', context)

