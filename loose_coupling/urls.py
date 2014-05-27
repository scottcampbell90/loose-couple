from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',

                       url(
                           r'^$',
                           TemplateView.as_view(template_name='index.html'),
                           name='home'
                       ),

                       url(
                           r'',
                           include('account.urls'),
                       ),

                       url(
                           r'^admin/',
                           include(admin.site.urls)
                       ),

                       )+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
