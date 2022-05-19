from django.shortcuts import render
from .models import Person
from django.db.models import Q

# Create your views here.
def Search(request):
    # if 'q' in request.GET:
    msg = None
    if 'q' in request.GET:
        search = request.GET['q']
        if search != '':
            multiple_q = Q(Q(first_name__iexact=search) | Q(last_name__iexact=search))
            data = Person.objects.filter(multiple_q)
            if data.exists() == False:
                msg = 'No results for this search'
    else:
        data = Person.objects.all()
    return render(request, 'dashboard/base.html', {'data': data, 'msg': msg})
