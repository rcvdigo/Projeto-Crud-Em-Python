from django.shortcuts import render, redirect
from appCrud.forms import CarrosForm
from appCrud.models import Carros
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


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
    form = CarrosForm(request.POST or None)
    re = request.POST
    if form.is_valid():
        form.save()

        # Verifica se a requisição foi feita pelo Postman
        user_agent = request.headers.get('User-Agent', '')
        if 'Postman' in user_agent:
            # Se a requisição foi feita pelo Postman, salva os dados no banco de dados
            # Aqui você pode adicionar lógica para salvar os dados do formulário no banco de dados
            # Substitua esta linha pela lógica real para salvar os dados no banco de dados

            # Exemplo:
            # novo_carro = form.save(commit=False)
            # novo_carro.save()

            return JsonResponse(
                {
                    'message': 'Dados salvos no banco de dados via Postman',
                    'request': re,
                    'form': form
                }, status=201)
        else:
            return redirect('home')  # Redireciona para 'home' se a requisição não foi feita pelo Postman
    else:
        return JsonResponse({'error': 'Erro de validação'}, status=400)

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
