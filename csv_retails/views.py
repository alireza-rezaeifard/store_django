from django.shortcuts import render, HttpResponse, redirect
import csv
from .models import Fashion
from .forms import FashionForm

def import_csv(request):
    with open(r'store_django\csv_retails\retails.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Fashion.objects.create(
                Customer_Reference_ID=row['Customer_Reference_ID'],
                Item_Purchased=row['Item_Purchased'],
                Purchase_Amount=row['Purchase_Amount'],
                Review_Rating=row['Review_Rating'],
                Payment_Method=row['Payment_Method']
            )
    return HttpResponse('Data imported successfully!')

def add_data(request):
    if request.method == 'POST':
        form = FashionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_data')
    else:
        form = FashionForm()
    return render(request, 'add_data.html', {'form': form})
