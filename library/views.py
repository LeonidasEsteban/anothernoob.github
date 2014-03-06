from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from endless_pagination.decorators import page_template

from library.models import File
from library.models import Articles

import json

@csrf_exempt
@require_POST
@login_required
def upload_photos(request):
    images = []
    for f in request.FILES.getlist("file"):
        obj = File.objects.create(upload=f, is_image=True)
        images.append({"filelink": obj.upload.url})
    return HttpResponse(json.dumps(images), mimetype="application/json")

@login_required
def recent_photos(request):
    images = [
        {"thumb": obj.upload.url, "image": obj.upload.url}
        for obj in File.objects.filter(is_image=True).order_by("-date_created")[:20]
    ]
    return HttpResponse(json.dumps(images), mimetype="application/json")

def article_list(request):
    article_list = Articles.objects.filter(published = True).order_by('-date')
    try:
        article_promoted = Articles.objects.filter(published = True, promoted = True).order_by('-date')[0]
    except:
        article_promoted = None
    article_list_template = 'article_list_template.html'
    context = {
        'article_list': article_list,
        'article_list_template': article_list_template,
        'article_promoted': article_promoted,
    }
    template = 'article_list.html'
    if request.is_ajax():
        template = article_list_template
    return render_to_response(template ,context , context_instance = RequestContext(request))

def article_single(request, url_slug, article_id):
    try:
        article = Articles.objects.get(url_slug = url_slug, pk = article_id, published = True)
    except:
        article = get_object_or_404(Articles, pk = article_id, published = True)
        return HttpResponsePermanentRedirect('/article/%s/%s' % (article.url_slug, article.id))
    article_list = Articles.objects.filter(published = True, tags__name__in = article.tags.names()).distinct().exclude(pk = article.id).order_by('-date')
    comments_template = 'article_comments.html'
    context = {
        'article': article,
        'article_list': article_list,
        'comments_template': comments_template,
    }
    template = 'article_single.html'
    if request.is_ajax():
        template = comments_template
    return render_to_response(template, context, context_instance = RequestContext(request))

def backbone_article_list(request):
    if request.method == 'GET':
        try:
            articles = Articles.objects.filter(published = True)
            article_list = [article.as_json() for article in articles]
            return HttpResponse(json.dumps(article_list), mimetype = "application/json")
        except:
            raise Http404

def backbone_news(request):
    try:
        article_promoted = Articles.objects.filter(published = True, promoted = True).order_by('-date')[0]
    except:
        article_promoted = None
    context = {
        'article_promoted': article_promoted,
    }
    template = 'backbone_article_list.html'
    return render_to_response(template ,context , context_instance = RequestContext(request))

def get_email(request):
    if request.method == 'POST' and request.POST.get('email'):
        request.session['saved_username'] = request.POST['email']
        backend = request.session['partial_pipeline']['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('get_email.html', {}, context_instance = RequestContext(request))

def preview_article(request, url_slug, article_id):
    try:
        article = Articles.objects.get(url_slug = url_slug, pk = article_id)
    except:
        article = get_object_or_404(Articles, pk = article_id)
        return HttpResponsePermanentRedirect('/preview/%s/%s' % (article.url_slug, article.id))
    article_list = Articles.objects.filter(published = True, tags__name__in = article.tags.names()).distinct().exclude(pk = article.id)
    comments_template = 'article_comments.html'
    context = {
        'article': article,
        'article_list': article_list,
        'comments_template': comments_template,
    }
    template = 'article_single.html'
    if request.is_ajax():
        template = comments_template
    return render_to_response(template, context, context_instance = RequestContext(request))