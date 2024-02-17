from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmacia
from .forms import FarmaciaForm

def record_list(request):
    records = Farmacia.objects.all()
    return render(request,'record_list.html', {'records': records})

def record_create(request):
    form = FarmaciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('record_list')
    return render(request, 'record_form.html', {'form': form})

def record_update(request, pk):
    record = get_object_or_404(Farmacia, pk=pk)
    form = FarmaciaForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('record_list')
    return render(request, 'record_form.html', {'form': form})

def record_delete(request, pk):
    record = get_object_or_404(Farmacia, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'record_confirm_delete.html', {'record': record})
