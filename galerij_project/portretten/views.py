from django.shortcuts import render
from .models import Basisgegevens, Beroep

def index(request):
    return render(request, 'portretten/index.html')

def objects(request, template='portretten/objects.html', page_template='portretten/object_list.html'):
    objects = Basisgegevens.objects.order_by('nummer')
    filter = request.GET.get('filter', '')

    match filter:
        case "ambacht":
            objects = objects.filter(beroep=3)
        case "bank":
            objects = objects.filter(beroep=6)
        case "bibliotheek":
            objects = objects.filter(beroep=18)
        case "film":
            objects = objects.filter(beroep=20)
        case "gsw":
            objects = objects.filter(beroep=14)
        case "gezondheid":
            objects = objects.filter(beroep=12)
        case "handel":
            objects = objects.filter(beroep=5)
        case "kunst":
            objects = objects.filter(beroep=19)
        case "landbouw":
            objects = objects.filter(beroep=1)
        case "leger":
            objects = objects.filter(beroep=11)
        case "mijnbouw":
            objects = objects.filter(beroep=2)
        case "natuurwetenschap":
            objects = objects.filter(beroep=13)
        case "bestuur":
            objects = objects.filter(beroep=8)
        case "opvoeding":
            objects = objects.filter(beroep=16)
        case "overige":
            objects = objects.filter(beroep=23)
        case "pers":
            objects = objects.filter(beroep=17)
        case "politiek":
            objects = objects.filter(beroep=9)
        case "recht":
            objects = objects.filter(beroep=10)
        case "religie":
            objects = objects.filter(beroep=21)
        case "sociaal":
            objects = objects.filter(beroep=15)
        case "sport":
            objects = objects.filter(beroep=22)
        case "techniek":
            objects = objects.filter(beroep=4)
        case "transport":
            objects = objects.filter(beroep=7)
        case "zonder":
            objects = objects.filter(beroep=24)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        template = page_template

    context = {
        'objects': objects,
        'count': objects.count(),
        'filter': filter,
        'page_template': page_template,
    }

    return render(request, template, context)
