from django.shortcuts import render, redirect

def check_profile(request):
	if request.session['saved_first_bane']:
		backend = request.session['partial_pipeline']['backend']
		return redirect('socialauth_complete', backend = backend)