from django.contrib import admin
from .models import *

try:
    admin.site.register(Province)
    admin.site.register(Organisation)
    admin.site.register(Property)
    admin.site.register(Taxon)
    admin.site.register(AnnualPopulation)
except NameError:
    # If any model name doesn't exist in your wildlife/models.py, you can skip it safely.
    pass
