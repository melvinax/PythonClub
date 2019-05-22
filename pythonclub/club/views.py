from django.shortcuts import render
from .models import ProductType

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def clubtypes (request):
    type_list=ProductsType.objects.all()
    context={'types_list' : types_list }
    return render (request, 'club/types.html',  context=context)
