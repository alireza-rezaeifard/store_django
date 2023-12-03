from django.shortcuts import render, HttpResponse, redirect
import csv
from .models import Fashion
from .forms import FashionForm, SearchForm
from django.db.models import Q
from django.conf import settings
import os



def import_csv(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'csv_retails', 'retails.csv')
    
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Fashion.objects.create(
                Customer_Reference_ID=row['Customer_Reference_ID'],
                Item_Purchased=row['Item_Purchased'],
                Purchase_Amount=row['Purchase_Amount'],
                Date_Purchase=row['Date Purchase'],
                Review_Rating=row['Review_Rating'],
                Payment_Method=row['Payment_Method']
            )
    return HttpResponse('Data imported successfully!')

def search_csv(request):
    query = request.GET.get('q', '')
    results = []

    csv_file_path = os.path.join(settings.BASE_DIR, 'csv_retails', 'retails.csv')

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # اگر query در هر یک از فیلدها وجود داشته باشد، این ردیف به نتایج اضافه می‌شود.
            if any(query.lower() in str(row[field]).lower() for field in row.keys()):
                results.append(row)

    return render(request, 'search_csv.html', {'results': results, 'query': query})

def add_data(request):
    if request.method == 'POST':
        form = FashionForm(request.POST)
        if form.is_valid():
            form.save()

            # ذخیره‌ی داده‌های ورودی در فایل CSV
            csv_file_path = os.path.join(settings.BASE_DIR, 'csv_retails', 'retails.csv')
            with open(csv_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    form.cleaned_data['Customer_Reference_ID'],
                    form.cleaned_data['Item_Purchased'],
                    form.cleaned_data['Purchase_Amount'],
                    form.cleaned_data['Date_Purchase'],
                    form.cleaned_data['Review_Rating'],
                    form.cleaned_data['Payment_Method'],
                ])

            return redirect('add_data')
    else:
        form = FashionForm()
    return render(request, 'add_data.html', {'form': form})

def search_data(request):
    form = SearchForm(request.GET)

    if form.is_valid():
        search_field = form.cleaned_data.get('search_field')
        search_term = form.cleaned_data.get('search_term')

        csv_file_path = os.path.join(settings.BASE_DIR, 'csv_retails', 'retails.csv')
        results = []

        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # اگر هیچ فیلدی انتخاب نشده باشد، تمام ردیف‌ها را نشان بده
                if not search_field:
                    results.append(row)
                # در غیر این صورت فیلتر کن
                elif row.get(search_field) == search_term:
                    results.append(row)

        return render(request, 'search_data.html', {'form': form, 'results': results})

    return render(request, 'search_data.html', {'form': form, 'results': []})

