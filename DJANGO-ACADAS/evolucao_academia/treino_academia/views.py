from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Medidas, Pernas, Costas
from .forms import MedidasForm, PernasForm, CostasForm

#View Medidas
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

#View Costas  
def costas_list(request):
    costas = Costas.objects.all()
    return render(request, 'costas_list.html', {'costas': costas})

def costas_create(request):
    form = CostasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('costas_list')
    return render(request, 'costas_form.html', {'form': form})

def costas_update(request, pk):
    costas = get_object_or_404(Costas, pk=pk)
    form = CostasForm(request.POST or None, instance=costas)
    if form.is_valid():
        form.save()
        return redirect('costas_list')
    return render(request, 'costas_form.html', {'form': form})

def costas_delete(request, pk):
    costas = get_object_or_404(Pernas, pk=pk)
    if request.method == 'POST':
        costas.delete()
        return redirect('costas_list')
    return render(request, 'costas_delete.html', {'costas': costas})

# views Pernas
def pernas_list(request):
    pernas = Pernas.objects.all()
    return render(request, 'pernas_list.html', {'pernas': pernas})

def pernas_create(request):
    form = PernasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pernas_list')
    return render(request, 'pernas_form.html', {'form': form})

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