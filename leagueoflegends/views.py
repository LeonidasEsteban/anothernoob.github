# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from leagueoflegends.models import Players
from leagueoflegends.forms import SummonerForm

import os

from leagueoflegends.models import Champions

def champion_list(request):
    environ = os.environ
    champion_list = Champions.objects.all()
    return render_to_response('test.html', {'champion_list': champion_list, 'environ': environ}, context_instance = RequestContext(request))

def league_index(request):
	if request.method == 'POST':
		form = SummonerForm(request.POST)
		if form.is_valid():
			data = SummonerForm.cleaned_data['nickname']
	template = 'league.html'
	try:
		summoner = Players.objects.get(user = request.user)
	except:
		summoner = None
	context = {
    	'summoner': summoner,
    	'summonerForm': SummonerForm
    }
	return render_to_response(template, context, context_instance = RequestContext(request))