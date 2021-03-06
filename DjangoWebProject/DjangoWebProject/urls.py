"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
	url(r'^imageTypeConverter$', app.views.imageTypeConverter, name='imageTypeConverter'),
    url(r'^imageSizeConverter$', app.views.imageSizeConverter, name='imageSizeConverter'),
    url(r'^imageAddFilter$', app.views.imageAddFilter, name='imageAddFilter'),
    url(r'^imageGrayscale$', app.views.imageGrayscale, name='imageGrayscale'),
    url(r'^imageRotate$', app.views.imageRotate, name='imageRotate'),
    url(r'^imageContrast$', app.views.imageContrast, name='imageContrast')

        # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
