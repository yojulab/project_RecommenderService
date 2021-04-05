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
       contact_list = dml_mongodb.find(db_name=db_name, collaction_name=collaction_name, data=data['request'])           # get Collection with find()
       data['page_obj'] = contact_list
    except:
        pass
    finally:
        pass
    
    return render(request, 'home/list.html', context=data)
