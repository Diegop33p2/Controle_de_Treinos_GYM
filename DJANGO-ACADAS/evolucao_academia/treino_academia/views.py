from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Medidas, Pernas
from .forms import MedidasForm, PernasForm

def record_list(request):
    records = Medidas.objects.all()
    return render(request,'record_list.html', {'records':records})

def record_create(request):
    form = MedidasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('record_list')
    return render(request, 'record_form.html', {'form' :form})

def record_update(request, pk):
    record = get_object_or_404(Medidas, pk=pk)
    form = MedidasForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('record_list')
    return render(request, 'record_form.html', {'form' :form})

def record_delete(request, pk):
    record = get_object_or_404(Medidas, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'record_delete.html', {'record': record})
    
   
def pernas_list(request):
    pernas = Pernas.objects.all()
    return render(request, 'pernas_list.html', {'pernas': pernas})

def pernas_create(request):
    form = PernasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pernas_list')
    return render(request, 'pernas_form.html', {'form': form})

# def pernas_create(request):
#     form = PernasForm(request.POST or None)
#     if request.method == 'POST':
#         print("Dados do formulário recebidos:", request.POST)
#         if form.is_valid():
#             print("Formulário válido")
#             form.save()
#             return redirect('pernas_list')
#         else:
#             print("Erros de validação no formulário:", form.errors)
#     return render(request, 'pernas_form.html', {'form': form})

def pernas_update(request, pk):
    pernas = get_object_or_404(Pernas, pk=pk)
    form = PernasForm(request.POST or None, instance=pernas)
    if form.is_valid():
        form.save()
        return redirect('pernas_list')
    return render(request, 'treinos_form.html', {'form': form})

def pernas_delete(request, pk):
    pernas = get_object_or_404(Pernas, pk=pk)
    if request.method == 'POST':
        pernas.delete()
        return redirect('pernas_list')
    return render(request, 'pernas_delete.html', {'pernas': pernas})