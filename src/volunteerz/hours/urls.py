from django.conf.urls import url


from .views import (
     HoursListView, 
    HoursDetailView, 
    HoursLocationCreateView
    )


urlpatterns = [
    url(r'^$', HoursListView.as_view(),name='list'),
   # url(r'^create2/$', HoursCreateView),
    url(r'^create/$', HoursLocationCreateView.as_view(),name='create'),
    url(r'^(?P<slug>[\w-]+)/$', HoursDetailView.as_view(),name='detail'),
]
