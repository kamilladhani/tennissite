from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic import View, FormView, DetailView, ListView, TemplateView

import os
import models

# Create your views here.

def playerpage(request):
	context = {}
	return render(request, 'players/playerpage.html', context)
	
def mens(request):
	context = {}
	return render(request, 'players/mens.html', context)
	
def womens(request):
	context = {}
	return render(request, 'players/womens.html', context)


	
"""
class PlayerDetail(DetailView):

    model = models.player
    context_object_name =  "player"
    template_name = "players.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PlayerDetail, self).get_context_data(*args, **kwargs)
        return context
"""
