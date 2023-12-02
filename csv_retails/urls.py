# myapp/urls.py
from django.urls import path
from .views import import_csv, add_data, search_data

urlpatterns = [
    path('import-csv/', import_csv, name='import_csv'),
    path('add-data/', add_data, name='add_data'),
    path('search-data/', search_data, name='search_data'),
]
