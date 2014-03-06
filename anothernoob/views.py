from django.contrib.auth import logout
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from library.models import Articles

def cait_vi(request):
    return render_to_response('cait_vi.html', context_instance = RequestContext(request))

def get_email(request):
    if request.method == 'POST' and request.POST.get('email'):
        request.session['saved_email'] = request.POST['email']
        backend = request.session['partial_pipeline']['backend']
        return redirect('socialauth_complete', backend = backend)
    return render_to_response('get_email.html', {}, RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def search_view(request, search_string):
    article_result = Articles.objects.filter(Q(title__icontains = search_string) | Q(summary__icontains = search_string) | Q(content__icontains = search_string))
    result = article_result
    try:
        article_promoted = Articles.objects.filter(published = True, promoted = True).order_by('date')[0]
    except:
        article_promoted = None
    article_list_template = 'article_list_template.html'
    context = {
        'article_list': result,
        'article_list_template': article_list_template,
        'article_promoted': article_promoted,
    }
    template = 'search.html'
    if request.is_ajax():
        template = article_list_template
    return render_to_response(template ,context , context_instance = RequestContext(request))