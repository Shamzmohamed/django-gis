# Django GIS Farm Management

## Project Overview
This project is a Django GIS application for managing **Farms**, **Fields**, and **Irrigation Points**, extended with full **CRUD Class-Based Views (CBVs)** and GIS features using GeoDjango.

---
## 📌 Branch Overview

| Branch | Description |
|--------|--------------|
| **main** | Models with GIS fields, migrations, and fully configured Django Admin. |
| **django-lesson-2-orm** | Wildlife app added + all ORM query tasks implemented via `run_orm` command. |
| **django-lesson-3-cbv** | Full CRUD using Class-Based Views (CBVs) for Farm + Field, BaseModel improvements, templates, pagination, messages. |
| **django-lesson-4-fbv** | Function-Based Views (FBVs) with CRUD for Farm + Field, BaseModel integration, auto-updating fields, read-only restrictions, messages, and pagination. |
| **django-lesson-5-test** | Complete test suite for Wildlife ORM queries using Django TestCase, including edge cases and aggregation validation. |

---
## Features
- GeoDjango models using `PointField` and `PolygonField`
- Django Admin with search, filtering, and interactive GIS map widgets
- CRUD operations implemented with **Class-Based Views** for:
  - Farm
  - Field
- Shared BaseModel with:
  - `last_update` (auto-updated)
  - `last_update_by` (auto-updated with logged-in user)
- Metadata fields are **read-only** in forms
- Success messages for create/update/delete
- Pagination on list pages
- Simple navigation menu for smooth user flow

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Shamzmohamed/django-gis.git
cd django-gis
```
2. **Install dependencies**
```
pip install -r requirements.txt
```
3. **Apply Migrations**
```
python manage.py makemigrations
python manage.py migrate
```
4. **Create a superuser (optional)**
```
python manage.py createsuperuser
```
5. **Run development server**
```
python manage.py runserver
```
6. **Access Django admin**
```
http://127.0.0.1:8000/admin/
```
---
### ORM Assignment Tasks (Assignment 2)
```
git checkout django-lesson-2-orm  #Switch to branch 2
python manage.py run_orm
```
```
All 12 ORM tasks are implemented in:
wildlife/management/commands/run_orm.py
```
---
### CRUD Views (Assignment 3)
Two models from the farming app (Farm & Field) have full CRUD operations using Class-Based Views:
```
git checkout django-lesson-3-cbv  #Switch to branch 3
```
## 🌐 CRUD URLs
**Farms**
```
List → http://127.0.0.1:8000/farms/
Create → http://127.0.0.1:8000/farms/add/
Detail → http://127.0.0.1:8000/farms/<id>/
Update → http://127.0.0.1:8000/farms/<id>/edit/
Delete → http://127.0.0.1:8000/farms/<id>/delete/
```
**Fields**
```
List → http://127.0.0.1:8000/fields/
Create → http://127.0.0.1:8000/fields/add/
Detail → http://127.0.0.1:8000/fields/<id>/
Update → http://127.0.0.1:8000/fields/<id>/edit/
Delete → http://127.0.0.1:8000/fields/<id>/delete/
```
### Function Based Views - FBV (Assignment 4)
```
Features:
Paginated list views
Auto-update last_update and last_update_by
Success messages
Clean UI templates
```
**Example URL Patterns**
```
path("farms/", farm_list, name="farm_list"),
path("farms/add/", farm_create, name="farm_create"),
path("farms/<int:pk>/", farm_detail, name="farm_detail"),
path("farms/<int:pk>/edit/", farm_update, name="farm_update"),
path("farms/<int:pk>/delete/", farm_delete, name="farm_delete"),
```
