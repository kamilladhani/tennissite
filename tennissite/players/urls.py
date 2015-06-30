from django.conf import settings
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy, reverse

import views

urlpatterns = patterns('',
	url(r'^$', views.playerpage, name="playerpage"),
	url(r'^mens/$', views.mens, name="mens"),
	url(r'^womens/$', views.womens, name="womens"),
)
