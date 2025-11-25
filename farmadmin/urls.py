from django.urls import path
from . import views

urlpatterns = [
    # FARM FBVs
    path("farms/", views.farm_list, name="farm_list"),
    path("farms/add/", views.farm_create, name="farm_create"),
    path("farms/<int:pk>/", views.farm_detail, name="farm_detail"),
    path("farms/<int:pk>/edit/", views.farm_update, name="farm_update"),
    path("farms/<int:pk>/delete/", views.farm_delete, name="farm_delete"),

    # FIELD FBVs
    path("fields/", views.field_list, name="field_list"),
    path("fields/add/", views.field_create, name="field_create"),
    path("fields/<int:pk>/", views.field_detail, name="field_detail"),
    path("fields/<int:pk>/edit/", views.field_update, name="field_update"),
    path("fields/<int:pk>/delete/", views.field_delete, name="field_delete"),
]
