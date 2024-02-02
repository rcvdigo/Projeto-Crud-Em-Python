from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from appCrud.forms import CarrosForm
from appCrud.models import Carros


# Create your views here.
def home(request):
    data = {}
    escolha1 = request.GET.get('marca-search')
    escolha2 = request.GET.get('modelo-search')
    search = request.GET.get('search')
    if search:
        if(escolha1):
            data['db'] = Carros.objects.filter(marca__icontains=search)        
        elif(escolha2):
            data['db'] = Carros.objects.filter(modelo__icontains=search)
        else:
            data['db'] = Carros.objects.all()
           
    else:
        all = Carros.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data ={}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)


@csrf_exempt
def create(request):
    if request.method == 'POST':
        # if request.headers.get('content-type') == 'application/json':  # Verifica se a requisição é JSON
        # Se a requisição é JSON, carrega os dados do corpo da requisição
        data = request.POST.dict()
        form = CarrosForm(data)
        # else:
        # Se a requisição é via formulário HTML, usa request.POST diretamente
        form = CarrosForm(request.POST)

        return JsonResponse(
            {
                'postman': request.POST.dict(),
                'form_html': request.POST
            }
        )

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')
