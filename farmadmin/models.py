# farmadmin/models.py
from django.contrib.gis.db import models  # using GeoDjango for geometry fields
from django.core.exceptions import ValidationError
from .base import BaseModel

# 1️⃣ Farm model — main farm record
class Farm(BaseModel):
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    area = models.FloatField(help_text="Total area of the farm in hectares")
    location = models.PointField(srid=4326)  # geometry field (point location of the farm)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.owner_name})"

    def clean(self):
        # Basic validation: area must be positive
        if self.area is not None and self.area <= 0:
            raise ValidationError({"area": "Area must be greater than 0."})

# 2️⃣ Field model — represents specific crop fields within a farm
class Field(BaseModel):
    CROP_CHOICES = [
        ('wheat', 'Wheat'),
        ('corn', 'Corn'),
        ('rice', 'Rice'),
        ('barley', 'Barley'),
    ]

    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="fields")
    name = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=10, choices=CROP_CHOICES)
    boundary = models.PolygonField(srid=4326)  # geometry field (polygon boundary)
    area = models.FloatField(help_text="Area of this field (ha)")
    planted_on = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.crop_type})"

    def clean(self):
        if self.area is not None and self.area <= 0:
            raise ValidationError({"area": "Field area must be greater than 0."})

# 3️⃣ IrrigationPoint model — represents irrigation infrastructure in a field
class IrrigationPoint(BaseModel):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="irrigation_points")
    point_id = models.CharField(max_length=50)
    location = models.PointField(srid=4326)  # geometry field (point)
    water_source = models.CharField(max_length=100, help_text="Water source (well, canal, etc.)")
    installed_on = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.point_id} ({self.field.name})"
