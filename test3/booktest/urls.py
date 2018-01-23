from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(\d+)/(\d+)/(\d+)/$',views.detail,name='detail'),
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$',views.getTest2),
    url(r'^getTest3/$',views.getTest3),

    url(r'^postTest1/$',views.postTest1),
    url(r'^postTest2/$',views.postTest2),
]
