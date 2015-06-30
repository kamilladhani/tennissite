from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic import View, FormView, DetailView, ListView, TemplateView

import os
import models
from forms import NameForm

# Create your views here.


def homepage(request):
	context = {}
	return render(request, 'home/homepage.html', context)

class HomeUser(DetailView):
	model = models.User
	context_object_name = "user"
	template_name = "home/homepage.html"

	def get_context_data(self, *args, **kwargs):
	    context = super(HomeUser, self).get_context_data(*args, **kwargs)
	    return context


class NameView(FormView):
	template_name = "home/info.html"
	form_class = NameForm
	
	def form_valid(self, form):
		data = form.cleaned_data
		firstname = data['firstname']
		lastname = data['lastname']
		new = models.User(firstname=firstname, lastname=lastname)
		new.save()
		return HttpResponseRedirect(reverse("home:homeuser", kwargs={"pk":new.pk}))
