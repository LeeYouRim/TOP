from django.shortcuts import render
from .models import todays
from django.http import HttpResponse
from django.contrib.auth.models import User
import xlwt

# Create your views here.

def index(requets):
    todayranks = todays.objects.all()
    return render(requets, "index.html", {"todayranks":todayranks})

def excel_export(request):
    response = HttpResponse(content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename="todaysrank.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('today')
    row_num = 0
    col_names = ['category', 'title', 'brand', 'today']
    for idx, col_name in enumerate(col_names):
        ws.write(row_num, idx, col_name)

    rows = todays.objects.all().values_list('category', 'title', 'brand', 'today')
    for row in rows:
        row_num +=1
        for col_num, attr in enumerate(row):
            ws.write(row_num, col_num, attr)

    wb.save(response)
    return response