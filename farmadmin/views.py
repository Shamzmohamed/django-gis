# farmadmin/views.py
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib import messages
from django.shortcuts import redirect
from .models import Farm, Field

# -------------------------
# FARM CRUD VIEWS
# -------------------------
class FarmListView(ListView):
    model = Farm
    template_name = "farmadmin/farm_list.html"
    context_object_name = "farms"
    paginate_by = 10  # pagination

class FarmDetailView(DetailView):
    model = Farm
    template_name = "farmadmin/farm_detail.html"
    context_object_name = "farm"

class FarmCreateView(CreateView):
    model = Farm
    template_name = "farmadmin/farm_form.html"
    fields = ["name", "owner_name", "area", "location"]
    success_url = reverse_lazy("farm_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Create"
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        # set last_update_by to current user if available
        if self.request.user.is_authenticated:
            obj.last_update_by = self.request.user
        obj.save()
        messages.success(self.request, "Farm created successfully.")
        return super().form_valid(form)

class FarmUpdateView(UpdateView):
    model = Farm
    template_name = "farmadmin/farm_form.html"
    fields = ["name", "owner_name", "area", "location"]
    success_url = reverse_lazy("farm_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Update"
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user.is_authenticated:
            obj.last_update_by = self.request.user
        obj.save()
        messages.success(self.request, "Farm updated successfully.")
        return super().form_valid(form)

class FarmDeleteView(DeleteView):
    model = Farm
    template_name = "farmadmin/farm_confirm_delete.html"
    success_url = reverse_lazy("farm_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Farm deleted successfully.")
        return super().delete(request, *args, **kwargs)


# -------------------------
# FIELD CRUD VIEWS
# -------------------------
class FieldListView(ListView):
    model = Field
    template_name = "farmadmin/field_list.html"
    context_object_name = "fields"
    paginate_by = 10

class FieldDetailView(DetailView):
    model = Field
    template_name = "farmadmin/field_detail.html"
    context_object_name = "field"

class FieldCreateView(CreateView):
    model = Field
    template_name = "farmadmin/field_form.html"
    fields = ["farm", "name", "crop_type", "boundary", "area", "planted_on"]
    success_url = reverse_lazy("field_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Create"
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user.is_authenticated:
            obj.last_update_by = self.request.user
        obj.save()
        messages.success(self.request, "Field created successfully.")
        return super().form_valid(form)

class FieldUpdateView(UpdateView):
    model = Field
    template_name = "farmadmin/field_form.html"
    fields = ["farm", "name", "crop_type", "boundary", "area", "planted_on"]
    success_url = reverse_lazy("field_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Update"
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user.is_authenticated:
            obj.last_update_by = self.request.user
        obj.save()
        messages.success(self.request, "Field updated successfully.")
        return super().form_valid(form)

class FieldDeleteView(DeleteView):
    model = Field
    template_name = "farmadmin/field_confirm_delete.html"
    success_url = reverse_lazy("field_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Field deleted successfully.")
        return super().delete(request, *args, **kwargs)