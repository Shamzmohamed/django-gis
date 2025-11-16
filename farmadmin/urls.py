from django.urls import path
from .views import (
    FarmListView, FarmDetailView, FarmCreateView, FarmUpdateView, FarmDeleteView,
    FieldListView, FieldDetailView, FieldCreateView, FieldUpdateView, FieldDeleteView
)

urlpatterns = [

    # FARM CRUD
    path("farms/", FarmListView.as_view(), name="farm_list"),
    path("farms/<int:pk>/", FarmDetailView.as_view(), name="farm_detail"),
    path("farms/add/", FarmCreateView.as_view(), name="farm_create"),
    path("farms/<int:pk>/edit/", FarmUpdateView.as_view(), name="farm_update"),
    path("farms/<int:pk>/delete/", FarmDeleteView.as_view(), name="farm_delete"),

    # FIELD CRUD
    path("fields/", FieldListView.as_view(), name="field_list"),
    path("fields/<int:pk>/", FieldDetailView.as_view(), name="field_detail"),
    path("fields/add/", FieldCreateView.as_view(), name="field_create"),
    path("fields/<int:pk>/edit/", FieldUpdateView.as_view(), name="field_update"),
    path("fields/<int:pk>/delete/", FieldDeleteView.as_view(), name="field_delete"),
]