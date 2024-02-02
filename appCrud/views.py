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


# @csrf_exempt
# def create(request):
#     if request.method == 'POST':
#         form = CarrosForm(request.POST)
#         form_type = type(form).__name__
#         if form.is_valid():
#             try:
#                 car = form.save()
#                 if request.is_ajax():
#                     return JsonResponse({'car_id': car.id}, status=201)
#                 else:
#                     return JsonResponse({'message': 'Carro criado com sucesso'}, status=201)
#             except ValueError as e:
#                 return JsonResponse({'error_message': str(e)}, status=400)
#         else:
#             return JsonResponse({'error_message': 'Formulário inválido'}, status=400)
#     else:
#         return JsonResponse({'error_message': 'Apenas solicitações POST são permitidas'}, status=405)



@api_view(['POST'])
@csrf_exempt
def create(request):
    if request.method == 'POST':
        # Verifica se a requisição é JSON
        if 'application/json' in request.content_type:
            data_api = request.data
            form = CarrosForm(data_api)
        else:
            data_html = request.POST
            form = CarrosForm(data_html)
        
        if form.is_valid():
            car = form.save()
            if data_api:
                Response(
                    {
                        'message': 'Carro criado com sucesso',
                        'post_man': data_api
                    }, status=status.HTTP_201_CREATED
                )
            if data_html:
                Response(
                    {
                        'message': 'Carro criado com sucesso',
                        'html': data_html
                    }, status=status.HTTP_201_CREATED
                )
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


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
