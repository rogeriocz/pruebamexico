from django.conf.urls import patterns, include, url
from .views import signup, signin


urlpatterns = patterns('',
   
   url(r'^registro/$', signup, name='signup'),
   url(r'^entrar/$', userprofiles.signin, name='signin'),
   

)