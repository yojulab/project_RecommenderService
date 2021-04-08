from django.http import HttpResponse
import csv
from home.mongopaginator import MongoPaginator
import sys
import os
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render		# add


def home(request):
    return render(request, 'home/home.html')


def list(request):
    data = dict()
    data['request'] = request.GET.copy()
    sys.path.append(os.getcwd())

    from libraries import dml_mongodb
    db_name = 'db_scraping'
    collaction_name = 'periodicity_scraping'

    try:
        # get Collection with find()
        contact_list = dml_mongodb.find(
            db_name=db_name, collaction_name=collaction_name, data=data['request'])
        lineperpage = 20              # Show 15 contacts per page.
        paginator = MongoPaginator(contact_list, lineperpage)

        page_number = request.GET.get('page', 1)
        data['page_obj'] = paginator.get_page(page_number)
    except:
        pass
    finally:
        pass

    return render(request, 'home/list.html', context=data)


def export_csv(request):
    data = dict()
    data['request'] = request.GET.copy()
    sys.path.append(os.getcwd())

    from libraries import dml_mongodb
    db_name = 'db_scraping'
    collaction_name = 'periodicity_scraping'

    try:
        # get Collection with find()
        contact_list = dml_mongodb.find(
            db_name=db_name, collaction_name=collaction_name, data=data['request'])
    except:
        pass
    finally:
        pass

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csv.writer(response)
    writer.writerow(['모집 주제', '상세링크', '마감일', '경력', '학력', '근무지역', '회사명'])

    fromlist = ['recruit_title', 'detail_url', 'apply_end_date', 'need_career', 'need_education', 'work_place', 'company_name']
    for row in contact_list:
        data = { key : row.get(key) for key in fromlist }
        if data['recruit_title']:
            writer.writerow(data.values())
    return response
