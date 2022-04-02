from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()

    #data['db'] = Carros.objects.all()
    #all = Carros.objects.all() #variavel All que recebe todos os registros
    #paginator = Paginator(all, 5) #paginação que recebe todos os registros, mas exibe somente 2(ou o numero que estiver ali)
    #pages = request.GET.get('page') #pegamos via get em nossa URL um parametro pages e vamos paginar de acordo com a linha 13 (formatação)
    #data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}   #criar um dicionario
    data['form'] = CarrosForm()  #chamar um campo FORM desse dicionario e ele recebe o CarrosForm()
    return render(request, 'form.html', data) #mandar o data la pra dentro do form.html

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request,'view.html',data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request,'form.html',data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form= CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')