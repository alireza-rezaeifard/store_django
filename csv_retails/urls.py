# myapp/urls.py
from django.urls import path
from .views import import_csv, add_data, search_data, index, delete_confirmation_view, delete_record_view
from . import views


urlpatterns = [
    path('import-csv/', import_csv, name='import_csv'),
    path('add-data/', add_data, name='add_data'),
    path('search-data/', search_data, name='search_data'),
    path('search-csv/', views.search_csv, name='search_csv'),
    path('', index, name='index'),
    path('delete-confirmation/<int:result_id>/', delete_confirmation_view, name='delete_confirmation'),
    path('delete-record/<int:result_id>/', delete_record_view, name='delete_record'),
]
