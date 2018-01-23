from django.shortcuts import render
from .models import *
from django.db.models import Max,F,Q

def index(request):
    # list=BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    # list=BookInfo.books1.filter(pk__lte=3)
    # max1=BookInfo.books1.aggregate(Max('id'))
    # list=BookInfo.books1.filter(bread__gt=F('bcommet'))
    # list=BookInfo.books1.filter(pk__lt=4,btitle__contains='1')与下面==
    # list=BookInfo.books1.filter(pk__lt=4).filter(btitle__contains='1')
    list=BookInfo.books1.filter(Q(pk__lt=4)|Q(btitle__contains='八'))
    context={
        'list':list,
        # 'max1':max1

             }

    return render(request,'booktest/index.html',context)
