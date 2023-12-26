from django.shortcuts import render, HttpResponse, redirect, reverse
import csv
from .models import Fashion
from .forms import FashionForm, SearchForm
from django.db.models import Q
from django.conf import settings
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404



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
            if any(query.lower() in str(row[field]).lower() for field in row.keys()):
                results.append(row)

    # ایجاد یک شیء Paginator با 50 ردیف در هر صفحه
    paginator = Paginator(results, 50)

    # درخواست مربوط به صفحه را دریافت
    page = request.GET.get('page')

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # اگر شماره صفحه عدد نباشد، نشان دادن اولین صفحه
        results = paginator.page(1)
    except EmptyPage:
        # اگر شماره صفحه بیشتر از تعداد صفحات باشد، نشان دادن آخرین صفحه
        results = paginator.page(paginator.num_pages)

    return render(request, 'search_csv.html', {'results': results, 'query': query})

def add_data(request):
    form_submitted = False

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

            form_submitted = True
    else:
        form = FashionForm()

    return render(request, 'add_data.html', {'form': form, 'form_submitted': form_submitted})

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



def index(request):
    return render(request, 'index.html')


