from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Farm, Field
from .forms import FarmForm, FieldForm

# ---------- FARM FBVs ----------
def farm_list(request):
    farms = Farm.objects.order_by('-last_update')
    paginator = Paginator(farms, 10)
    page = request.GET.get('page')
    farms = paginator.get_page(page)
    return render(request, "farmadmin/farm_list.html", {"farms": farms})

def farm_detail(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    return render(request, "farmadmin/farm_detail.html", {"farm": farm})

@login_required
def farm_create(request):
    form = FarmForm(request.POST or None)
    if form.is_valid():
        farm = form.save(commit=False)
        farm.last_update_by = request.user
        farm.save()
        messages.success(request, "Farm created successfully!")
        return redirect("farm_list")
    return render(request, "farmadmin/farm_form.html", {"form": form, "action": "Create"})

@login_required
def farm_update(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    form = FarmForm(request.POST or None, instance=farm)
    if form.is_valid():
        farm = form.save(commit=False)
        farm.last_update_by = request.user
        farm.save()
        messages.success(request, "Farm updated successfully!")
        return redirect("farm_detail", pk=farm.pk)
    return render(request, "farmadmin/farm_form.html", {"form": form, "action": "Update"})

@login_required
def farm_delete(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == "POST":
        farm.delete()
        messages.success(request, "Farm deleted successfully!")
        return redirect("farm_list")
    return render(request, "farmadmin/farm_confirm_delete.html", {"farm": farm})


# ---------- FIELD FBVs ----------
def field_list(request):
    fields = Field.objects.order_by('-last_update')
    paginator = Paginator(fields, 10)
    page = request.GET.get('page')
    fields = paginator.get_page(page)
    return render(request, "farmadmin/field_list.html", {"fields": fields})

def field_detail(request, pk):
    field = get_object_or_404(Field, pk=pk)
    return render(request, "farmadmin/field_detail.html", {"field": field})

@login_required
def field_create(request):
    form = FieldForm(request.POST or None)
    if form.is_valid():
        field = form.save(commit=False)
        field.last_update_by = request.user
        field.save()
        messages.success(request, "Field created successfully!")
        return redirect("field_list")
    return render(request, "farmadmin/field_form.html", {"form": form, "action": "Create"})

@login_required
def field_update(request, pk):
    field = get_object_or_404(Field, pk=pk)
    form = FieldForm(request.POST or None, instance=field)
    if form.is_valid():
        field = form.save(commit=False)
        field.last_update_by = request.user
        field.save()
        messages.success(request, "Field updated successfully!")
        return redirect("field_detail", pk=field.pk)
    return render(request, "farmadmin/field_form.html", {"form": form, "action": "Update"})

@login_required
def field_delete(request, pk):
    field = get_object_or_404(Field, pk=pk)
    if request.method == "POST":
        field.delete()
        messages.success(request, "Field deleted successfully!")
        return redirect("field_list")
    return render(request, "farmadmin/field_confirm_delete.html", {"field": field})
