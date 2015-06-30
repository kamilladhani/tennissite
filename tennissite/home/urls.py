from django.conf import settings
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy, reverse

import views

urlpatterns = patterns('',
	url(r'^$', views.homepage, name="homepage"),
	url(r'^(?P<pk>\d+)/$', views.HomeUser.as_view(), name="homeuser"),
	url(r'^info', views.NameView.as_view(), name="infopage"),
)