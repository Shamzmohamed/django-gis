# Django GIS Farm Management

## Project Overview

This Django project demonstrates a **farm management system** with GIS capabilities using **GeoDjango**.  
The system includes three models:

1. **Farm** – Represents a farm owned by a farmer. Each farm has:
   - Name
   - Owner Name
   - Total area (hectares)
   - Geographic location (PointField)
   - Creation date

2. **Field** – Represents a crop section within a farm. Each field has:
   - Name
   - Crop type (choices: Wheat, Corn, Rice, Barley)
   - Boundary (PolygonField)
   - Area (hectares)
   - Planted on date
   - Foreign key linking it to a Farm

3. **IrrigationPoint** – Represents irrigation infrastructure for a field. Each point has:
   - Point ID
   - Location (PointField)
   - Water source
   - Installed on date
   - Foreign key linking it to a Field

The models are fully linked via foreign keys:

This allows hierarchical tracking of farms, fields, and irrigation points with real-world GIS mapping.

---

## Features

- **GeoDjango integration:**  
  All models with spatial fields (PointField and PolygonField) display interactive maps in the Django admin using OpenLayers.

- **Admin interface customization:**
  - `list_display` shows multiple columns per model
  - `search_fields` allows searching by key attributes (e.g., Farm name, Field name, Point ID)
  - `list_filter` enables filtering by crop type and farm
  - `raw_id_fields` for foreign keys enables efficient lookup for large datasets

- **Custom `__str__` methods:**  
  Makes admin displays human-readable, e.g., `Wheat Field 1 (Wheat)` instead of `Field object (1)`.

- **Migrations:**  
  All models have migrations applied successfully.

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/django-gis.git
cd django-gis
