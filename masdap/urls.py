from django.conf.urls import patterns, url
# from django.views.generic import TemplateView

from geonode.urls import *

urlpatterns = patterns('',
   url(r'^/?$', TemplateView.as_view(template_name='site_index.html'), name='home'),#
#   url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
   url(r'^account/signup/', include('account_captcha.urls')), 
   url(r'^contact/', include('contact.urls')),
 ) + urlpatterns
