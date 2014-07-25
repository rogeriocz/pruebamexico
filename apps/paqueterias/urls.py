from django.conf.urls import patterns, include, url
from .views import IndexView


urlpatterns = patterns('',
   
   url(r'^paquete/', IndexView.as_view())
   

)