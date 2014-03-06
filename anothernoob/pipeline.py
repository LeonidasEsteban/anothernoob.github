from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from social.models import UserProfile

def check_social(request, user, *args, **kwargs):
	try:
		profile = UserProfile.objects.get(user = user)
	except:
		profile = UserProfile(user = user)
		profile.save()